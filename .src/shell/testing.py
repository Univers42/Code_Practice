import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

from exam_config import ExamConfig
from restrictions import parse_forbidden_functions, used_forbidden_functions

REPO_ROOT = Path(__file__).resolve().parents[2]


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


def tester_c(config: ExamConfig) -> list[Any]:
    return _fail(config, "ERROR: C testing is not implemented yet")


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
