from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["42"],
    ["-17"],
    ["0"],
    ["   99abc"],
    ["abc"],
    ["  +5"],
    [""],
    ["2147483647"],
    ["-2147483648"],
    ["   -42   "],
]
