#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = my_list[0]
    for num in my_list:
        if num > max_int:
            max_int = num
    return max_int


'''
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
'''
