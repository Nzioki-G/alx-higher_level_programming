#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for idx_curr, num in enumerate(my_list):
        if idx_curr == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[idx_curr])
    return new_list
