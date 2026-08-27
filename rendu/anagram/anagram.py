def anagram(s1: str, s2: str) -> bool:
    new1: str = s1.replace(" ", "")
    new2: str = s2.replace(" ", "")

    new1 = new1.upper()
    new2 = new2.lower()

    return sorted(new1) == sorted(new2)