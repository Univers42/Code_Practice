def anagram_solution(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False

    new1: str = s1.replace(" ", "")
    new2: str = s2.replace(" ", "")

    new1 = new1.lower()
    new2 = new2.lower()

    return sorted(new1) == sorted(new2)
