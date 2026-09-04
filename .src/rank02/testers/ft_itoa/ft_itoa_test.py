from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["0"],
    ["1"],
    ["-1"],
    ["42"],
    ["-42"],
    ["2147483647"],
    ["-2147483648"],
    ["100"],
    ["-100"],
]
