from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["zaz"],
    ["dub0 a POIL"],
    [""],
    ["a"],
    ["ab"],
    [],
    ["step on no pets"],
    ["1 2 3 4 5"],
]
