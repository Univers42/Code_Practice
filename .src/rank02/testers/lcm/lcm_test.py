from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['4', '6'],
    ['21', '6'],
    ['0', '5'],
    ['5', '0'],
    ['7', '7'],
    ['1', '1'],
    ['17', '13'],
    ['46337', '46341'],
]
