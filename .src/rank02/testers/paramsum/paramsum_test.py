from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1', '2', '3', '5', '7', '24'],
    ['6', '12', '24'],
    [],
    ['a'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
]
