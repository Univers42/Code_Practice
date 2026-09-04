from dataclasses import dataclass, field
from pathlib import Path

from constants import (
    EXERCISES_02,
    EXERCISES_02_BY_NAME,
    EXERCISES_3,
    EXERCISES_4,
)

REPO_ROOT = Path(__file__).resolve().parents[3]


@dataclass
class ExamConfig:
    rank: int
    exercise_names: list[str]
    levels: int
    subjects_dir: str
    current_exercise: str = ""
    retrys: int = 0
    level: int = 0
    last_failure_time: float = 0.0
    # name -> "program" / "function" for ranks that turn in C (rank 02).
    # Empty for Python ranks, where the distinction doesn't apply.
    exercise_kinds: dict[str, str] = field(default_factory=dict)

    def kind_of(self, name: str) -> str:
        return self.exercise_kinds.get(name, "")

    def exercise_pool(self) -> list[int]:
        return list(range(len(self.exercise_names)))

    def score_after(self, passed: int) -> int:
        return passed * 100 // self.levels

    def points_for_level(self, level: int) -> int:
        return self.score_after(level + 1) - self.score_after(level)

    @property
    def last_level(self) -> int:
        return self.levels - 1


_RANK_DATA = {
    2: (EXERCISES_02, 4, ".subjects/rank02"),
    3: (EXERCISES_3, 6, ".subjects/rank03"),
    4: (EXERCISES_4, 4, ".subjects/rank04"),
}


def get_exam_config(rank: int) -> ExamConfig:
    exercise_names, levels, subjects_dir = _RANK_DATA[rank]
    exercise_kinds = (
        {name: ex.kind for name, ex in EXERCISES_02_BY_NAME.items()}
        if rank == 2
        else {}
    )
    return ExamConfig(
        rank, exercise_names, levels, subjects_dir,
        exercise_kinds=exercise_kinds,
    )


def _check_rank02_layout(name: str) -> list[str]:
    """rank02 turns in C: solutions/<ex>/<ex>.c (+ main.c for FUNCTION) and
    testers/<ex>/<ex>_test.py with the argv cases."""
    problems: list[str] = []
    src = REPO_ROOT / ".src" / "rank02"
    sol_dir = src / "solutions" / name
    if not (sol_dir / f"{name}.c").is_file():
        problems.append(f"rank02/{name}: missing solutions/{name}/{name}.c")
    exercise = EXERCISES_02_BY_NAME.get(name)
    if exercise is not None and exercise.kind == "function":
        if not (sol_dir / "main.c").is_file():
            problems.append(f"rank02/{name}: missing solutions/{name}/main.c")
    if not (src / "testers" / name / f"{name}_test.py").is_file():
        problems.append(f"rank02/{name}: missing testers/{name}/{name}_test.py")
    return problems


def validate_rank_data() -> list[str]:
    problems: list[str] = []
    for rank, (exercise_names, levels, subjects_dir) in _RANK_DATA.items():
        if levels > len(exercise_names):
            problems.append(
                f"rank{rank:02d}: levels ({levels}) exceeds the number of "
                f"exercises available ({len(exercise_names)})"
            )
        rank_dir = f"rank{rank:02d}"
        extension = "c" if rank == 2 else "py"
        for name in exercise_names:
            subject_dir = REPO_ROOT / subjects_dir / name
            if not subject_dir.is_dir():
                problems.append(f"rank{rank:02d}/{name}: missing subject dir")
            if rank == 2:
                problems.extend(_check_rank02_layout(name))
                continue
            solution_file = (
                REPO_ROOT / ".src" / rank_dir / "solutions" / name
                / f"{name}_solution.{extension}"
            )
            tester_file = (
                REPO_ROOT / ".src" / rank_dir / "testers" / name
                / f"{name}_test.{extension}"
            )
            if not solution_file.is_file():
                problems.append(
                    f"rank{rank:02d}/{name}: missing solution file"
                )
            if not tester_file.is_file():
                problems.append(f"rank{rank:02d}/{name}: missing tester file")
    return problems
