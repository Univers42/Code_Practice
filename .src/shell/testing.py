import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

from exam_config import ExamConfig

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot build an import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_trace(config: ExamConfig, content: str) -> None:
    """Persist a failure report to traces/<level>_<retry>_<exercise>.txt."""
    traces_dir = Path("traces")
    traces_dir.mkdir(exist_ok=True)
    filename = f"{config.level}_{config.retrys}_traces_{config.current_exercise}.txt"
    (traces_dir / filename).write_text(content)


def _fail(config: ExamConfig, message: str) -> list[Any]:
    """Persist the failure message to traces/ and return the failure result."""
    _write_trace(config, message)
    return [message, False]


def choice_test(config: ExamConfig) -> list[Any]:
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

    solution_module = _load_module(f"{exercise}_solution", solution_path)
    solution_fn = getattr(solution_module, f"{exercise}_solution")

    tester_module = _load_module(f"{exercise}_test", tester_path)
    test_cases = tester_module.TEST_CASES

    try:
        rendu_module = _load_module(exercise, rendu_path)
        rendu_fn = getattr(rendu_module, exercise)
    except (OSError, ImportError, SyntaxError) as error:
        return _fail(config, f"ERROR: {error}")
    except AttributeError:
        return _fail(config, f"ERROR: no function named '{exercise}' in your file")
    report: list[Any] = []
    passed = True
    for n, test in enumerate(test_cases, 1):
        my_result = solution_fn(*test)
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
