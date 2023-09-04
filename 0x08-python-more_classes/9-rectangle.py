#!/usr/bin/python3
"""A square is a rectangle"""


class Rectangle:
    '''defines a rectangle that can be defined from a square'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''instantiates with optional width and height'''
        Rectangle.number_of_instances += 1
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
            rect += str(self.print_symbol * self.__width)
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''instantiates a rectangle where height == width == size'''
        return cls(size, size)


"""
my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(),
my_square.perimeter()))
print(my_square)
"""
