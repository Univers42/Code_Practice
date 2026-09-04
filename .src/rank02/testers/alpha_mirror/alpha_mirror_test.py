from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["abc"],
    ["My horse is Amazing."],
    [""],
    ["a", "b"],
    [],
    ["ZzAa"],
    ["Hello, World! 123"],
    ["   spaces   "],
    ["UPPER lower MiXeD"],
    ["z"],
    ["A"],
]
