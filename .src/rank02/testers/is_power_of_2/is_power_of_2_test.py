from typing import Any

# Each case: a list of argv (strings passed after the program name),
# or {"argv": [...], "stdin": "..."}.
TEST_CASES: list[Any] = [
    ['1'],
    ['2'],
    ['3'],
    ['4'],
    ['1024'],
    ['1023'],
    ['0'],
    ['2147483648'],
    ['4294967295'],
    # a wide, scattered spread on both sides — a hardcoded lookup table
    # would need to enumerate all of these (and every other power of 2
    # up to 2^31) to fake its way past this, at which point it's not a
    # shortcut anymore, it's just writing the real function badly.
    ['8'], ['16'], ['32'], ['64'], ['128'], ['256'], ['512'],
    ['2048'], ['4096'], ['65536'], ['8388608'], ['536870912'],
    ['6'], ['10'], ['33'], ['63'], ['65'], ['100'], ['257'],
    ['1000'], ['12345'], ['999999'], ['33554431'], ['3000000000'],
]
