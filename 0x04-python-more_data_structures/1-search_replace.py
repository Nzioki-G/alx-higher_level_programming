#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    # append(replace) if i == search for each i in list
    new_list = [replace if i == search else i for i in my_list]
    return new_list
