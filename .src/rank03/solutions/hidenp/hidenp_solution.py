def hidenp_solution(small: str, big: str) -> bool:
    limit: int = len(small)
    if limit == 0:
        return True
    i: int = 0
    for char in big:
        if char == small[i]:
            i += 1
        if i == limit:
            return True
    return False
