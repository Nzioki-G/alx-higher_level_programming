#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    '''defines a rectangle init, area, perimeter'''

    def __init__(self, width=0, height=0):
        '''instantiates with optional width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''gets the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets / updates width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets / updates height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''returns the rectangular area'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the rectangular perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2


"""
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
my_rectangle.perimeter()))
"""
