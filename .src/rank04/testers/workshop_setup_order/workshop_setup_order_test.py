from typing import Any

TEST_CASES: list[list[Any]] = [
    [{"app": ["database"], "database": ["driver"], "driver": []}],
    [{"A": [], "B": ["A"], "C": ["A", "B"]}],
    [{"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}],
    [{}],
    [{"A": ["Z"]}],
    [{"A": ["A"]}],
    [{"X": ["Y"], "Y": ["X"]}]
]
