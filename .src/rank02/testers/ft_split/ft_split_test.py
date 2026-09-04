from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["hello world"],
    ["  leading and trailing  "],
    ["one\ttwo\nthree"],
    ["single"],
    [""],
    ["   "],
    ["a b  c   d"],
]
