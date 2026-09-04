from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1', '3'],
    ['-1', '2'],
    ['0', '0'],
    ['0', '-3'],
    ['-5', '5'],
    ['10', '1'],
    ['1', '5000'],
    ['-2500', '2500'],
]
