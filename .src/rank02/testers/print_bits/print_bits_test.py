from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['2'],
    ['0'],
    ['255'],
    ['128'],
    ['1'],
]


def random_cases(rng) -> list[Any]:
    """A fresh spread of bytes every run — nothing fixed to memorize."""
    return [[str(rng.randint(0, 255))] for _ in range(15)]
