from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["12fdb3", "16"],
    ["12FDB3", "16"],
    ["0123", "4"],
    ["-42", "10"],
    ["777", "8"],
    ["101", "2"],
    ["-101", "2"],
    ["ff", "16"],
    ["9", "2"],
    ["0", "10"],
]
