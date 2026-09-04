from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['42'],
    ['-17'],
    ['0'],
    ['   99abc'],
    ['abc'],
    ['  +5'],
    [''],
    ['2147483647'],
    ['-2147483648'],
    ['   -42   '],
    ['007'],
    ['+42'],
    ['-'],
    ['+'],
    ['\t\n  -42'],
]

_PREFIXES = ["", " ", "  ", "\t", "\n ", "   \t"]


def random_cases(rng) -> list[Any]:
    cases = []
    for _ in range(10):
        n = rng.randint(-2**31, 2**31 - 1)
        prefix = rng.choice(_PREFIXES)
        sign = "" if n < 0 else rng.choice(["", "+"])
        digits = str(abs(n)) if sign else str(n)
        cases.append([f"{prefix}{sign}{digits}"])
    return cases
