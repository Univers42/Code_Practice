from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['2'],
    ['0'],
    ['255'],
    ['128'],
    ['1'],
    ['170'],
]
