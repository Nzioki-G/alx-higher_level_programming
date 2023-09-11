#!/usr/bin/python3
'''Improve Geometry'''


class BaseGeometry:
    '''base geo with area()'''

    def area(self):
        '''raises an exception'''
        raise Exception("area() is not implemented")


"""
bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""
