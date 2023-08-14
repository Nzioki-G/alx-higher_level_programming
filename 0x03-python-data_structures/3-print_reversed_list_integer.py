#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    last = len(my_list)
    for idx in range(last - 1, -1, -1):
        print("{:d}".format(my_list[idx]))


"""
my_list = None
print_reversed_list_integer(my_list)
"""
