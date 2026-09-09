import random
import time

from constants import EXERCISES_02_LEVELS


def pick_random_exercise(exercises: list[int]) -> int:
    random.seed(time.time_ns())
    index = random.randrange(len(exercises))
    return exercises.pop(index)


def _rank02_level_pool(level: int) -> list[int]:
    """Flat indices (into EXERCISES_02) of the exercises that make up
    difficulty group `level`: 0 -> "Level 1", 1 -> "Level 2", and so on.
    The flat exercise list is exactly EXERCISES_02_LEVELS concatenated in
    order, so each group is one contiguous slice of it."""
    level = max(0, min(level, len(EXERCISES_02_LEVELS) - 1))
    offset = 0
    for index, (_, group) in enumerate(EXERCISES_02_LEVELS):
        if index == level:
            return list(range(offset, offset + len(group)))
        offset += len(group)
    return []


def pick_exam_exercise(rank: int, level: int, pool: list[int]) -> int:
    """rank 2 real exam: a random exercise drawn from the current
    difficulty group (progress level N is picked from
    EXERCISES_02_LEVELS[N]). Every other rank: a uniform random draw from
    `pool`, which is popped so an exercise never comes up twice in one
    exam."""
    if rank == 2:
        candidates = _rank02_level_pool(level)
        random.seed(time.time_ns())
        return random.choice(candidates)
    return pick_random_exercise(pool)
