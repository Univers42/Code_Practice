from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['FOR PONY'],
    ['this        ...       is sparta, then again, maybe    not'],
    ['   '],
    ['a', 'b'],
    ['  lorem,ipsum  '],
    [''],
    [],
    ['single'],
]
