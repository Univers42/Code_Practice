from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
# av[1] = space-separated ints, one node per int.
TEST_CASES: list[Any] = [
    ["1 2 3"],
    [""],
    ["5"],
    ["-1 -2 -3"],
    ["10 20 30 40 50"],
]
