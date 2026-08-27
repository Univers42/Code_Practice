def gears_match_solution(gear_a: list[int], gear_b: list[int]) -> bool:
    if len(gear_a) != len(gear_b):
        return False
    if not gear_a:
        return True
    doubled = gear_a + gear_a
    n = len(gear_a)
    for start in range(n):
        if doubled[start:start + n] == gear_b:
            return True
    return False
