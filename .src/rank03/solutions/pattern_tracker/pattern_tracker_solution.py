def pattern_tracker_solution(text: str) -> int:
    last_num = None
    total = 0
    for char in text:
        if char.isdigit():
            if last_num is None:
                last_num = int(char)
                continue
            elif int(char) == last_num + 1:
                last_num += 1
                total += 1
            else:
                last_num = int(char)
        else:
            last_num = None
    return total
