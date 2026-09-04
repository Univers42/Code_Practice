from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["abc", "abc"],
    ["abc", "abd"],
    ["abc", "ab"],
    ["ab", "abc"],
    ["", ""],
    ["", "a"],
    ["a", ""],
    ["Abc", "abc"],
    ["abc", "Abc"],
    ["zzz", "aaa"],
]
