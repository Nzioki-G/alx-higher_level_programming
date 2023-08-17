#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    number = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    for idx, ch in enumerate(roman_string):
        current = roman_dict[ch]
        prev = roman_dict[roman_string[idx - 1]]
        if idx > 0 and prev < current:
            current -= (prev * 2)
        number += current
    return number


""" Roman to Integer test file


roman_number = "LX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
"""
