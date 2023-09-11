#!/usr/bin/python3
'''Only a subclass of'''


def inherits_from(obj, a_class):
    '''derived directly or indirectly from'''
    return (obj.__class__ != a_class
            and issubclass(obj.__class__, a_class))


"""
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
"""
