#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    last = len(my_list)
    for idx in range(last - 1, -1, -1):
        print("{:d}".format(my_list[idx]))


"""
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
"""
