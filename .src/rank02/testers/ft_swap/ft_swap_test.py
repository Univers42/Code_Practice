from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1', '2'],
    ['-5', '5'],
    ['0', '0'],
    ['42', '42'],
    ['2147483647', '-2147483648'],
    ['-1', '100'],
]
