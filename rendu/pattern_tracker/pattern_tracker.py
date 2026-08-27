def pattern_tracker(text: str) -> int:
    past_num = None
    total_num = 0
    for char in text:
        if char.isdigit():
            if past_num is None:
                past_num = int(char)
                continue
            elif past_num == int(char) - 1:
                total_num += 1
                past_num = int(char)
                continue
            else:
                past_num = int(char)
        else:
            past_num = None
    return total_num