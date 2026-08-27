from dataclasses import dataclass

from constants import EXERCISES_3, EXERCISES_4


@dataclass
class ExamConfig:
    """Stores which exam the user picked so the program can route to it.

    It also carries the mutable state of the running exam: the name of the
    exercise currently being worked on and how many times it has been
    retried.
    """

    rank: int
    exercise_names: list[str]
    levels: int
    subjects_dir: str
    current_exercise: str = ""
    retrys: int = 0

    def exercise_pool(self) -> list[int]:
        return list(range(len(self.exercise_names)))

    def score_after(self, passed: int) -> int:
        """Score reached after passing `passed` exercises.

        Points are spread dynamically so that passing the last exercise
        always lands exactly on 100.
        """
        return passed * 100 // self.levels

    def points_for_level(self, level: int) -> int:
        """Points awarded by the exercise at position `level` (0-based)."""
        return self.score_after(level + 1) - self.score_after(level)

    @property
    def last_level(self) -> int:
        """0-based index of the final exercise."""
        return self.levels - 1


_RANK_DATA = {
    3: (EXERCISES_3, 6, ".subjects/rank03"),
    4: (EXERCISES_4, 4, ".subjects/rank04"),
}


def get_exam_config(rank: int) -> ExamConfig:
    """Build a fresh config for `rank` so no exam state leaks between runs."""
    exercise_names, levels, subjects_dir = _RANK_DATA[rank]
    return ExamConfig(rank, exercise_names, levels, subjects_dir)
