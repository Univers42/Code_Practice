from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['faya', 'fgvvfdxcacpolhyghbreda'],
    ['faya', 'fgvvfdxcacpolhyghbred'],
    ['quarante deux', 'qfqfsudf arzgsayns tsregfdgs sjytdekuoixq '],
    ['error', 'rrerrrfiiljdfxjyuifrrvcoojh'],
    [],
    ['%s%n', '%s%n'],
    ['abc', 'abc'],
    ['abcd', 'abc'],
]
