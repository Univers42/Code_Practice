from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['5 3 8 1 9 2'],
    [''],
    ['1'],
    ['-3 -1 -2'],
    ['5 5 5 1 1'],
    ['10 9 8 7 6 5 4 3 2 1'],
    ['7 7 7 7 7 7'],
]


def random_cases(rng) -> list[Any]:
    cases = []
    for _ in range(8):
        n = rng.randint(0, 40)
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
        cases.append([" ".join(map(str, nums))])
    return cases
