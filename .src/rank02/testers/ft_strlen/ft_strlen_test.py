from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
# Driver parses av[1] and prints ft_strlen(av[1]).
TEST_CASES: list[Any] = [
    ["hello"],
    [""],
    ["a"],
    ["this is a considerably longer string than the others"],
    ["with\ttabs\tand things"],
    ["   spaces   "],
]
