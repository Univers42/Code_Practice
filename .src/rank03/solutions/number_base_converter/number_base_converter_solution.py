def number_base_converter_solution(
    number: str, from_base: int, to_base: int
) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"
    if decimal == 0:
        return "0"
    negative = decimal < 0
    decimal = abs(decimal)
    result = ""
    while decimal > 0:
        result = digits[decimal % to_base] + result
        decimal //= to_base
    return ("-" + result) if negative else result
