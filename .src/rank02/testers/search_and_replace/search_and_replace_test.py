from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ["Papache est un sabre", "a", "o"],
    ["zaz", "art", "zul"],
    ["zaz", "r", "u"],
    ["jacob", "a", "b", "c", "e"],
    ["ZoZ eT Dovid oiME le METol.", "o", "a"],
    ["wNcOre Un ExEmPle Pas Facilw a Ecrirw ", "w", "e"],
    ["hello", "x", "y"],
    [""],
    ["only one arg"],
]
