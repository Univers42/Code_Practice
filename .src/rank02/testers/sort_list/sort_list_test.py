from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['5 3 8 1 9 2'],
    [''],
    ['1'],
    ['-3 -1 -2'],
    ['5 5 5 1 1'],
    ['50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1'],
    ['7 7 7 7 7 7'],
]
