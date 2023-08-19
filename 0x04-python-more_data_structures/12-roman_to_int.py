#!/usr/bin/python3

def roman_to_int(roman_string):
    # converts a Roman numeral to an integer and returns an integer
    if type(roman_string) is not str or roman_string is none:
        return 0
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    res = 0
    for roman in reversed(roman_string):
        digit = roman_dict[roman]
        res += digit if res < digit * 5 else -digit
    return res
