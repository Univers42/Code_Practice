from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['38'],
    ['0'],
    ['255'],
    ['1'],
    ['128'],
    ['170'],
    # evenly spread across the whole byte range, so a hardcoded per-value
    # table is as much work as writing the real bit manipulation.
    ['3'], ['20'], ['37'], ['54'], ['71'], ['88'], ['105'], ['122'],
    ['139'], ['156'], ['173'], ['190'], ['207'], ['224'], ['241'],
]
