#!/usr/bin/python3
'''Same class or inherit from '''


def is_kind_of_class(obj, a_class):
    '''instance of or derived from'''
    return isinstance(obj, a_class)


"""
a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
"""
