from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["abc"],
    ["AkjhZ zLKIJz , 23y "],
    ["Les stagiaires du staff ne sentent pas toujours tres bon."],
    [""],
    ["z"],
    ["Z"],
    [],
    ["Hello, World!"],
]
