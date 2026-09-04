from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
# av[1] = reference int, av[2] = space-separated ints (the list).
TEST_CASES: list[Any] = [
    ["3", "1 3 5 3 7"],
    ["9", "1 2 3"],
    ["1", "1 1 1"],
    ["0", ""],
    ["-2", "-2 3 -2 -2 4"],
]
