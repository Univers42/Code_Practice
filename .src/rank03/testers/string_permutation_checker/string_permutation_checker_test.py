from typing import Any

TEST_CASES: list[list[Any]] = [
    ["a", "a"],
    ["abc", "abc"],
    ["abc", "cba"],
    ["ab", "ba"],
    ["aab", "aba"],
    ["", ""],
    ["aab", "abb"],
    ["abc", "Abc"],
    ["abc", "abcd"],
    ["", "a"]
]
