#!/usr/bin/python3
'''Integer validator'''


class BaseGeometry:
    '''base geo with area() and integer_validator()'''

    def area(self):
        '''raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''instance method that validates value'''
        if not value.__class__ == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""
bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""
