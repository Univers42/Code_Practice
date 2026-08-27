def echo_validator_solution(text: str) -> bool:
    if text == "":
        return False
    trimed_str: str = text.replace(" ", "")
    reversed_string: str = "" + trimed_str.lower()[::-1]
    return trimed_str.lower() == reversed_string