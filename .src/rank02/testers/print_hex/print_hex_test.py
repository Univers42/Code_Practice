from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['10'],
    ['255'],
    ['5156454'],
    ['0'],
    ['16'],
    [],
    ['1', '2'],
    ['2147483647'],
    ['1'],
]
