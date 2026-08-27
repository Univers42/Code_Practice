def string_sculptor_solution(text: str) -> str:
    upp: bool = False
    new_str: str = ""
    for char in text:
        if char.isalpha():
            if upp:
                new_str += char.upper()
                upp = False
            else:
                new_str += char.lower()
                upp = True
        else:
            new_str += char
            if char == " ":
                upp = False
    return new_str
