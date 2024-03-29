#!/usr/bin/python3
'''Full rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''inherits from basegeometry'''
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''implemented in child'''
        return self.__height * self.__width

    def __str__(self):
        '''[Rectangle] <width>/<height>'''
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)


"""
r = Rectangle(3, 5)

print(r)
print(r.area())
"""
