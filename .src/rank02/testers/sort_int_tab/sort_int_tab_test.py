from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['5 3 8 1 9 2'],
    [''],
    ['1'],
    ['-3 -1 -2'],
    ['5 5 5 1 1'],
    ['10 9 8 7 6 5 4 3 2 1'],
]
