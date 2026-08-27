import random
import time


def pick_random_exercise(exercises: list[int]) -> int:
    random.seed(time.time_ns())
    index = random.randrange(len(exercises))
    return exercises.pop(index)
