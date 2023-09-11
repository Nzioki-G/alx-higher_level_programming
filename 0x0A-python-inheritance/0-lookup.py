#!/usr/bin/python3
'''Lookup an object'''


def lookup(obj):
    """return a list of attributes and methods of an object"""
    return list(dir(obj))


"""
class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass


print(lookup(MyClass1))
print("***")
print(lookup(MyClass2))
print("***")
print(lookup(int))
"""
