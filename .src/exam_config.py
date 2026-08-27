from dataclasses import dataclass

from constants import EXERCISES_3, EXERCISES_4


@dataclass
class ExamConfig:
    """Stores which exam the user picked so the program can route to it."""

    rank: int
    exercise_names: list[str]
    levels: int
    subjects_dir: str

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


RANK_CONFIGS = {
    3: ExamConfig(3, EXERCISES_3, 6, ".subjects/rank03"),
    4: ExamConfig(4, EXERCISES_4, 4, ".subjects/rank04"),
}


def get_exam_config(rank: int) -> ExamConfig:
    return RANK_CONFIGS[rank]
