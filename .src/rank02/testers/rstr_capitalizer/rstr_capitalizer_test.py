from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    [],
    ['a FiRSt LiTTlE TESt'],
    ['SecONd teST A LITtle BiT   Moar comPLEX', '   But... This iS not THAT COMPLEX', '     Okay, this is the last 1239809147801 but not    the least    t'],
    ['single'],
    ['a'],
]
