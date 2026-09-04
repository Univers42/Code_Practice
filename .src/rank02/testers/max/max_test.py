from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['3 1 4 1 5 9 2 6'],
    [''],
    ['5'],
    ['-1 -2 -3'],
    ['0 0 0'],
    ['-5 3 -2 8 1'],
]
