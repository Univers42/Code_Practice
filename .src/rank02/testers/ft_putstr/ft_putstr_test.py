from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
# Driver parses av[1] and calls ft_putstr(av[1]).
TEST_CASES: list[Any] = [
    ["hello"],
    [""],
    ["a string with spaces"],
    ["tab\tand\tstuff"],
    ["42 is a number, not a word"],
    ["\n"],
]
