#!/usr/bin/python3
"""Detect instance deletion"""


class Rectangle:
    '''defines a rectangle area, perimeter, print, str, repr, del'''

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

    def __str__(self):
        '''returns a string representation of rectangle with # characters'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            rect += '\n'
        return rect

    def print(self):
        '''prints the string representation of this rectangle'''
        print(self.__str__)

    def __repr__(self):
        '''returns a string representation such that the return
        value can recreate a new instance by using eval()
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''prints message when an instance of rect is deleted'''
        print("Bye rectangle...")


"""
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
"""
