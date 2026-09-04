from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["hello"],
    [""],
    ["a"],
    ["with spaces"],
    ["12345"],
    ["UPPER lower MiXeD"],
]
