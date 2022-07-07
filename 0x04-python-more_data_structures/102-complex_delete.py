#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    for k in a_dictionary.copy():
        if a_dictionary[k] == value:
            del a_dictionary[k]
        else:
            continue
    return a_dictionary
