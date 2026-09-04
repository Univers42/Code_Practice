from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['7', '4', '11111111', '10001001', '10010001', '10110001', '11100001'],
    ['0', '0', '000', '000', '000'],
    ['1', '1', 'aba', 'bbb', 'aba'],
    ['0', '0', 'ab', 'cd'],
    ['2', '2', '121', '212', '121'],
    ['0', '0', '1'],
    ['1', '1', '111', '101', '111'],
]
