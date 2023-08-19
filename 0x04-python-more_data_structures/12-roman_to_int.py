#!/usr/bin/python3

def roman_to_int(roman_string):
    # converts a Roman numeral to an integer and returns an integer
    if type(roman_string) is not str or roman_string is none:
        return 0
    roman_digt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    intg = [roman_digt[x] for x in roman_string]
    res = 0
    for x in range(len(intg)):
        res += intg[x]
        if intg[x - 1] < intg[x] and x != 0:
            res -= (intg[x - 1] + intg[x - 1])
        return res
