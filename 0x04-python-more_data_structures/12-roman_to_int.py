#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string == str(roman_string) and roman_string:
        # init prev at first roman char
        prev = roman_string[0]
        number = 0

        for c in roman_string:
            # if the prev is a lesser value, subrtact.. else add
            if roman[prev] >= roman[c]:
                number += roman[c]
            else:
                number = number - roman[prev] + roman[c] - roman[prev]
            prev = c
        return number
    else:
        return 0
