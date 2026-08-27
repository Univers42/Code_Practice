def whisper_cipher_solution(text: str, shift: int) -> str:
    low: str = "abcdefghijklmnopqrstuvwxyz"
    upp: str = low.upper()
    shift = shift % len(low)
    new_string: str = ""
    i: int
    for char in text:
        i = 0
        if char.isupper():
            while char != upp[i]:
                i += 1
            new_string += upp[(i + shift) % len(low)]
        elif char.islower():
            while char != low[i]:
                i += 1
            new_string += low[(i + shift) % len(low)]
        else:
            new_string += char
    return new_string

