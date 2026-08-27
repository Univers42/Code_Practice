from dataclasses import dataclass
from pathlib import Path

from constants import EXERCISES_3, EXERCISES_4

REPO_ROOT = Path(__file__).resolve().parents[2]


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
    3: (EXERCISES_3, 6, ".subjects/rank03"),
    4: (EXERCISES_4, 4, ".subjects/rank04"),
}


def get_exam_config(rank: int) -> ExamConfig:
    exercise_names, levels, subjects_dir = _RANK_DATA[rank]
    return ExamConfig(rank, exercise_names, levels, subjects_dir)


def validate_rank_data() -> list[str]:
    problems: list[str] = []
    for rank, (exercise_names, levels, subjects_dir) in _RANK_DATA.items():
        if levels > len(exercise_names):
            problems.append(
                f"rank{rank:02d}: levels ({levels}) exceeds the number of "
                f"exercises available ({len(exercise_names)})"
            )
        rank_dir = f"rank{rank:02d}"
        for name in exercise_names:
            subject_dir = REPO_ROOT / subjects_dir / name
            solution_file = (
                REPO_ROOT / ".src" / rank_dir / "solutions" / name
                / f"{name}_solution.py"
            )
            tester_file = (
                REPO_ROOT / ".src" / rank_dir / "testers" / name
                / f"{name}_test.py"
            )
            if not subject_dir.is_dir():
                problems.append(f"rank{rank:02d}/{name}: missing subject dir")
            if not solution_file.is_file():
                problems.append(
                    f"rank{rank:02d}/{name}: missing solution file"
                )
            if not tester_file.is_file():
                problems.append(f"rank{rank:02d}/{name}: missing tester file")
    return problems
