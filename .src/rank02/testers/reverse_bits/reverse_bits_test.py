from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['38'],
    ['0'],
    ['255'],
    ['1'],
    ['128'],
    ['170'],
]
