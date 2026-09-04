from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1'],
    ['2'],
    ['4'],
    ['3'],
    ['0'],
]


def random_cases(rng) -> list[Any]:
    """Fresh, unpredictable each run: a lookup table would have to cover
    every power of 2 up to 2**31 plus a wide spread of non-powers to fake
    its way past this, which is no longer a shortcut over the real check."""
    cases = []
    for _ in range(10):
        cases.append([str(1 << rng.randint(0, 31))])
    for _ in range(10):
        n = rng.randint(0, 2**32 - 1)
        while n != 0 and (n & (n - 1)) == 0:
            n = rng.randint(0, 2**32 - 1)
        cases.append([str(n)])
    return cases
