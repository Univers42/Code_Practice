from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['4', '6'],
    ['21', '6'],
    ['0', '5'],
    ['5', '0'],
    ['7', '7'],
    ['1', '1'],
    ['17', '13'],
]


def random_cases(rng) -> list[Any]:
    cases = []
    for _ in range(10):
        a = rng.randint(0, 60000)
        b = rng.randint(0, 60000)
        cases.append([str(a), str(b)])
    return cases
