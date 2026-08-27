def inter_solution(s1: str, s2: str) -> str:
    new_string: str = ""
    for char1 in s1:
        for char2 in s2:
            if char1 == char2 and char1 not in new_string:
                new_string += char1
    return new_string
