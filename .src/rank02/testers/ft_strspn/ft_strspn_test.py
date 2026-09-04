from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['hello world', 'helo'],
    ['hello', 'abc'],
    ['hello', 'hello world'],
    ['', 'abc'],
    ['abc', ''],
    ['aaa', 'a'],
    ['   spaces', ' '],
]
