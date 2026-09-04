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
    # a single connected zone of 1600 cells (40x40, all one character):
    # an iterative flood fill backed by a small fixed-size queue/stack
    # (e.g. a hardcoded t_point queue[32]) silently stops early or
    # overflows well before covering this — only a structure that
    # actually grows with the zone gets every cell.
    ['0', '0'] + ['1' * 40] * 40,
]
