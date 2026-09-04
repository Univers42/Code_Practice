from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['42', '10'],
    ['42', '12'],
    ['14', '77'],
    ['17', '3'],
    ['100', '75'],
    [],
    ['5'],
    ['7', '7'],
    ['13', '17'],
    ['2147483647', '1'],
]
