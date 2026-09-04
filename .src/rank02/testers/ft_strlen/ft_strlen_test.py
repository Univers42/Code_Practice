import string
from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['hello'],
    [''],
    ['a'],
    ['this is a considerably longer string than the others'],
    ['with\ttabs\tand things'],
    ['   spaces   '],
]

_ALPHABET = string.ascii_letters + string.digits + " .,!?\t"


def random_cases(rng) -> list[Any]:
    cases = []
    for _ in range(8):
        length = rng.randint(0, 300)
        cases.append(["".join(rng.choice(_ALPHABET) for _ in range(length))])
    cases.append(["".join(rng.choice(_ALPHABET) for _ in range(rng.randint(2000, 4000)))])
    return cases
