from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["You hate people! But I love gatherings. Isn't it ironic?"],
    ['abcdefghijklm'],
    ['Wingardium Leviosa'],
    [],
    ['single'],
]
