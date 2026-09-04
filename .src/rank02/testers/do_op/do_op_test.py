from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['123', '*', '456'],
    ['9828', '/', '234'],
    ['1', '+', '-43'],
    ['10', '-', '3'],
    ['10', '%', '3'],
    ['0', '+', '0'],
    [],
    ['1', '+'],
    ['-7', '%', '3'],
    ['-7', '/', '2'],
    ['46340', '*', '46340'],
    ['-2147483647', '-', '1'],
]
