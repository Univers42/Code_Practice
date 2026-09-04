from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['5'],
    ['7'],
    ['1'],
    ['2'],
    ['0'],
    ['100'],
    ['-5'],
    ['abc'],
    [''],
    [],
    ['5', '6'],
    ['1000'],
    ['10000'],
]
