from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
# Driver parses av[1] as the source, copies into a fresh buffer, prints it.
TEST_CASES: list[Any] = [
    ["hello"],
    [""],
    ["abcdefghijklmnop"],
    ["with spaces inside"],
    ["digits 12345 and symbols !?"],
    ["a"],
]
