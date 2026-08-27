def bracket_validator_solution(s: str) -> bool:
    stack: list[str] = []
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
            continue
        if char == ")" or char == "}" or char == "]":
            if stack:
                temp = stack.pop()
            else:
                return False
            if temp == "(" and char == ")":
                continue
            elif temp == "[" and char == "]":
                continue
            elif temp == "{" and char == "}":
                continue
            else:
                return False

    return len(stack) == 0
