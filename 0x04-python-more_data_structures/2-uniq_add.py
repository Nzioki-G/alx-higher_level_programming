#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for elem in my_set:
        sum += elem
    return sum


"""
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
"""
