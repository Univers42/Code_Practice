from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['hello'],
    [''],
    ['a'],
    ['racecar'],
    ['ab'],
    ['a man a plan a canal panama'],
]
