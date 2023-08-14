#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""
    for cha in my_string:
        if cha == 'c' or cha == 'C':
            continue
        new_str += cha
    return new_str



print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

