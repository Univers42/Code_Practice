from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['abc   '],
    ['Que la      lumiere soit et la lumiere fut'],
    ['     AkjhZ zLKIJz , 23y'],
    ['first', '2', '11000000'],
    [],
    ['single'],
]
