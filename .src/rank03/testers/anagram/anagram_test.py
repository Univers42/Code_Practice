from typing import Any

TEST_CASES: list[list[Any]] = [
    ["hello", "bello"],
    ["lisen", "nisel"],
    ["acb", "cba"],
    ["cool", "looc"],
    ["Abc", "cba"],
    ["A B C", "abc"],
    ["lorem ipsum", "ipsum lorem"],
    ["dormitory", "dirty room"],
    ["a", "ab"],
    ["aaa", "aa"],
    ["", ""],
    ["what's happend with this? It is broken?", None],
    [None, "abc"]
    ]
