from typing import Any

TEST_CASES: list[list[Any]] = [
    ["abc", 0],
    ["XYZ", 1],
    ["Hello, World!", 3],
    ["abcXYZ", 13],
    ["abc", 26],
    ["abc", 27],
    ["abc", -1],
    ["", 5]
]
