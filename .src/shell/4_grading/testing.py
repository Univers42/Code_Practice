import importlib.util
import os
import random
import shutil
import tempfile
import time
from pathlib import Path
from types import ModuleType
from typing import Any

from c_build import SANITIZE_FLAGS, compile_binary, compile_object
from c_exec import run_binary
from c_malloc_probe import MALLOC_CHECKS, build_probe, check_allocations, run_with_probe
from c_report import describe_case, diff_text, same
from c_restrictions import forbidden_functions_used, parse_allowed_functions
from exam_config import ExamConfig
from restrictions import parse_forbidden_functions, used_forbidden_functions

REPO_ROOT = Path(__file__).resolve().parents[3]
RANK02_SRC = REPO_ROOT / ".src" / "rank02"


def _load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot build an import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_trace(config: ExamConfig, content: str) -> None:
    traces_dir = Path("traces")
    traces_dir.mkdir(exist_ok=True)
    filename = (
        f"{config.level}_{config.retrys}_traces_{config.current_exercise}.txt"
    )
    (traces_dir / filename).write_text(content)


def _fail(config: ExamConfig, message: str) -> list[Any]:
    _write_trace(config, message)
    return [message, False]


def choice_test(config: ExamConfig) -> list[Any]:
    if config.rank == 2:
        return tester_c(config)
    return tester_python(config)


def _load_c_cases(exercise: str) -> list[tuple[list[str], bytes]]:
    """Fixed TEST_CASES (if any) plus fresh random_cases(rng) (if the tester
    defines one) generated NOW, with a new seed every call. Nothing about
    them is stored on disk: reading the tester file, or even running the
    reference as an oracle beforehand, doesn't tell you what this run's
    random cases will be, which is the whole point — it closes off
    memorized/hardcoded lookup-table answers regardless of how visible the
    test files themselves are."""
    tester_path = RANK02_SRC / "testers" / exercise / f"{exercise}_test.py"
    module = _load_module(f"{exercise}_c_test", tester_path)
    raw_cases = list(getattr(module, "TEST_CASES", []))
    random_fn = getattr(module, "random_cases", None)
    if random_fn is not None:
        rng = random.Random(time.time_ns() ^ os.getpid())
        raw_cases.extend(random_fn(rng))
    cases: list[tuple[list[str], bytes]] = []
    for entry in raw_cases:
        if isinstance(entry, dict):
            argv = [str(a) for a in entry.get("argv", [])]
            stdin = entry.get("stdin", "")
        else:
            argv = [str(a) for a in entry]
            stdin = ""
        raw = stdin.encode() if isinstance(stdin, str) else bytes(stdin)
        cases.append((argv, raw))
    return cases


def _copy_c_files(src_dir: Path, dest: Path, skip: set[str] = frozenset()) -> list[str]:
    names: list[str] = []
    for path in sorted(src_dir.glob("*.c")):
        if path.name in skip:
            continue
        shutil.copy(path, dest / path.name)
        names.append(path.name)
    return names


def _copy_headers(src_dir: Path, dest: Path) -> None:
    for path in sorted(src_dir.glob("*.h")):
        shutil.copy(path, dest / path.name)


def _prepare_builds(
    config: ExamConfig, work: Path
) -> tuple[Path, Path, list[str], list[str], list[str]] | list[Any]:
    """Lay out ref/ and stu/ build dirs.

    Returns (ref, stu, ref_srcs, stu_srcs, stu_own_srcs) where stu_own_srcs
    is the subset of stu_srcs that is actually the student's code (excludes
    our injected main.c for FUNCTION exercises) — that's what the
    allowed-functions check must look at, not our own driver.
    """
    exercise = config.current_exercise
    kind = config.kind_of(exercise)
    sol_dir = RANK02_SRC / "solutions" / exercise
    rendu_dir = REPO_ROOT / "rendu" / exercise

    if not sol_dir.is_dir():
        return _fail(config, f"ERROR: no reference for {exercise}")
    if not list(rendu_dir.glob("*.c")):
        return _fail(
            config,
            f"ERROR: nothing turned in "
            f"(expected rendu/{exercise}/{exercise}.c)",
        )

    ref = work / "ref"
    stu = work / "stu"
    ref.mkdir()
    stu.mkdir()
    for dest in (ref, stu):
        shutil.copy(RANK02_SRC / "super.h", dest / "super.h")
        _copy_headers(sol_dir, dest)  # canonical headers win over the student's

    if kind == "function":
        driver = sol_dir / "main.c"
        if not driver.is_file():
            return _fail(config, f"ERROR: missing driver main.c for {exercise}")
        shutil.copy(driver, ref / "main.c")
        shutil.copy(driver, stu / "main.c")
        ref_srcs = ["main.c"] + _copy_c_files(sol_dir, ref, skip={"main.c"})
        stu_own_srcs = _copy_c_files(rendu_dir, stu)
        stu_srcs = ["main.c"] + stu_own_srcs
    else:
        ref_srcs = _copy_c_files(sol_dir, ref)
        stu_own_srcs = _copy_c_files(rendu_dir, stu)
        stu_srcs = stu_own_srcs

    return ref, stu, ref_srcs, stu_srcs, stu_own_srcs


def _check_allowed_functions(
    config: ExamConfig, stu_dir: Path, stu_own_srcs: list[str]
) -> list[Any] | None:
    """Only the student's own files, never the reference or our driver:
    the alumno can use whatever they want internally, this only checks what
    THEIR turn-in calls externally against the subject's whitelist."""
    exercise = config.current_exercise
    subject_path = REPO_ROOT / config.subjects_dir / exercise / "subject.en.txt"
    try:
        allowed = parse_allowed_functions(subject_path)
    except OSError:
        return None  # can't read the subject: don't block grading over it

    objects = []
    for src in stu_own_srcs:
        obj_build, obj_path = compile_object(stu_dir, src)
        if not obj_build.ok:
            return _fail(
                config, f"ERROR: your code does not compile:\n{obj_build.log}"
            )
        objects.append(obj_path)

    violations = forbidden_functions_used(objects, allowed)
    if violations:
        return _fail(
            config,
            f"ERROR: forbidden function(s) used: {', '.join(violations)}",
        )
    return None


def _check_malloc_sizes(
    config: ExamConfig, ref_dir: Path, stu_dir: Path, stu_srcs: list[str]
) -> list[Any] | None:
    """Disproportionate mallocs (malloc(1000000) for a 3-byte word, or
    malloc(strlen(whole_input)) reused for every item regardless of its
    own size) produce correct output, so the normal comparison can't see
    them. Rebuild WITHOUT sanitizers (-fsanitize=address installs its own
    allocator and conflicts with an LD_PRELOAD hook) and run under a
    malloc-logging shim on a handful of dedicated argv cases chosen to
    expose a uniform/oversized allocation strategy.

    The reference (ref_dir/bin, already an unsanitized build) shares the
    exact same driver as the student, so it's run under the same probe to
    learn which allocation sizes are just driver/libc noise (e.g. glibc's
    first buffered stdio write) and not something the student's code did.
    """
    exercise = config.current_exercise
    if exercise not in MALLOC_CHECKS:
        return None
    _, probe_cases = MALLOC_CHECKS[exercise]
    plain_build = compile_binary(stu_dir, stu_srcs, "bin_plain")
    if not plain_build.ok:
        return None  # already compiled with more flags moments ago; be lenient
    probe_so = build_probe(stu_dir)
    if probe_so is None:
        return None  # probe infra unavailable: don't block grading over it
    log_path = stu_dir / "malloc_probe.log"
    for argv in probe_cases:
        baseline = run_with_probe(ref_dir / "bin", argv, b"", probe_so, log_path)
        sizes = run_with_probe(stu_dir / "bin_plain", argv, b"", probe_so, log_path)
        problem = check_allocations(exercise, argv, sizes, baseline)
        if problem:
            return _fail(
                config,
                f"ERROR: disproportionate allocation for {exercise}"
                f" ({describe_case(argv, b'')}): {problem}",
            )
    return None


def tester_c(config: ExamConfig) -> list[Any]:
    exercise = config.current_exercise
    try:
        cases = _load_c_cases(exercise)
    except (OSError, ImportError, SyntaxError, AttributeError, ValueError,
            TypeError, IndexError) as error:
        return _fail(config, f"ERROR: exercise setup is broken: {error}")
    if not cases:
        return _fail(config, f"ERROR: no test cases defined for {exercise}")

    with tempfile.TemporaryDirectory(prefix=f"{exercise}_") as tmp:
        prepared = _prepare_builds(config, Path(tmp))
        if isinstance(prepared, list):  # _fail(...) short-circuit
            return prepared
        ref_dir, stu_dir, ref_srcs, stu_srcs, stu_own_srcs = prepared

        ref_build = compile_binary(ref_dir, ref_srcs, "bin")
        if not ref_build.ok:
            return _fail(
                config,
                f"ERROR: reference for {exercise} does not compile:\n"
                f"{ref_build.log}",
            )
        stu_build = compile_binary(
            stu_dir, stu_srcs, "bin", extra_flags=SANITIZE_FLAGS
        )
        if not stu_build.ok:
            return _fail(
                config,
                f"ERROR: your code does not compile:\n{stu_build.log}",
            )

        violation = _check_allowed_functions(config, stu_dir, stu_own_srcs)
        if violation is not None:
            return violation

        malloc_violation = _check_malloc_sizes(config, ref_dir, stu_dir, stu_srcs)
        if malloc_violation is not None:
            return malloc_violation

        report: list[Any] = []
        for n, (argv, stdin) in enumerate(cases, 1):
            expected = run_binary(ref_dir / "bin", argv, stdin)
            if expected.timed_out or expected.crashed:
                return _fail(
                    config,
                    f"ERROR: reference misbehaved on test {n} "
                    f"({describe_case(argv, stdin)})",
                )
            actual = run_binary(stu_dir / "bin", argv, stdin)
            if same(expected, actual):
                report.append(f"test {n} [OK]")
                continue
            report.append(
                f"test {n} [KO]\nInput: {describe_case(argv, stdin)}\n"
                f"{diff_text(expected, actual)}"
            )
            _write_trace(config, "\n".join(report))
            report.append(False)
            return report

    report.append(True)
    return report


def tester_python(config: ExamConfig) -> list[Any]:
    exercise = config.current_exercise
    rank_dir = f"rank{config.rank:02d}"

    solution_path = (
        REPO_ROOT / ".src" / rank_dir / "solutions" / exercise
        / f"{exercise}_solution.py"
    )
    tester_path = (
        REPO_ROOT / ".src" / rank_dir / "testers" / exercise
        / f"{exercise}_test.py"
    )
    rendu_path = REPO_ROOT / "rendu" / exercise / f"{exercise}.py"
    subject_path = (
        REPO_ROOT / config.subjects_dir / exercise / "subject.en.txt"
    )

    try:
        solution_module = _load_module(f"{exercise}_solution", solution_path)
        solution_fn = getattr(solution_module, f"{exercise}_solution")
        tester_module = _load_module(f"{exercise}_test", tester_path)
        test_cases = tester_module.TEST_CASES
    except (OSError, ImportError, SyntaxError, AttributeError) as error:
        return _fail(config, f"ERROR: exercise setup is broken: {error}")

    try:
        rendu_module = _load_module(exercise, rendu_path)
        rendu_fn = getattr(rendu_module, exercise)
    except (OSError, ImportError, SyntaxError) as error:
        return _fail(config, f"ERROR: {error}")
    except AttributeError:
        return _fail(
            config, f"ERROR: no function named '{exercise}' in your file"
        )

    try:
        forbidden = parse_forbidden_functions(subject_path)
        rendu_source = rendu_path.read_text()
    except OSError:
        forbidden, rendu_source = [], ""
    used = used_forbidden_functions(rendu_source, forbidden)
    if used:
        return _fail(
            config, f"ERROR: forbidden function(s) used: {', '.join(used)}"
        )

    report: list[Any] = []
    passed = True
    for n, test in enumerate(test_cases, 1):
        try:
            my_result = solution_fn(*test)
        except Exception as error:
            return _fail(
                config,
                f"ERROR: reference solution is broken on test {n} "
                f"(input: {test}): {error}",
            )
        try:
            your_result = rendu_fn(*test)
        except Exception as e:
            report.append(f"test {n} [KO]\nInput: {test}\nError: {e}")
            passed = False
            continue
        if my_result != your_result:
            report.append(
                f"test {n} [KO]\nInput: {test} \n"
                f"Expected: {my_result} -> Your output: {your_result}"
            )
            passed = False
            _write_trace(config, "\n".join(report))
            report.append(passed)
            return report
        else:
            report.append(f"test {n} [OK]")

    if not passed:
        _write_trace(config, "\n".join(report))
    report.append(passed)
    return report
