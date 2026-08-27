def string_permutation_checker_solution(s1: str, s2: str) -> bool:
    length = len(s1)
    other = 0
    for char in s1:
        if char in s2:
            other += 1
            continue
        else:
            return False
    return length == other
