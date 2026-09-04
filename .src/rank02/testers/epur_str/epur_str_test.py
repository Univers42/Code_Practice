from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["See? It's easy to print the same thing"],
    [' this        time it      will     be    more complex  . '],
    ['No S*** Sherlock...', 'nAw S*** ShErLaWQ...'],
    [''],
    ['   '],
    ['a'],
    [],
    ['\t\ttabs\t\tand\tspaces   '],
]
