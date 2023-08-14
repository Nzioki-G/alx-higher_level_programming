#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for cha in my_string:
        if cha == 'c' or cha == 'C':
            continue
        else:
            new_str += cha
    return new_str
