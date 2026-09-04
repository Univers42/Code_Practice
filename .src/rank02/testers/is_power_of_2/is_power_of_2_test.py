from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1'],
    ['2'],
    ['3'],
    ['4'],
    ['1024'],
    ['1023'],
    ['0'],
    ['2147483648'],
    ['4294967295'],
]
