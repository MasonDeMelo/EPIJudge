from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    result = "" 
    negative = x < 0
    x = abs(x)
    while x:
        result = digit_to_char(x%10) + result
        x = x//10 
    return ("-" if negative else "") + result


def string_to_int(s: str) -> int:
    sf = 1
    result = 0
    for char in reversed(s):
        if char == "-":
            return -result
        elif char == "+":
            print(result)
        else:
            result += sf * char_to_digit(char)
            sf *= 10
    return result 

def char_to_digit(c: str) -> int:
    return {"0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9}[c]

def digit_to_char(d: int) -> str:
    return {0 : "0",
            1 : "1",
            2 : "2",
            3 : "3",
            4 : "4",
            5 : "5",
            6 : "6",
            7 : "7",
            8 : "8",
            9 : "9"}[d]



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
