#!/usr/bin/python3
"""A circle in code"""


class MagicClass:
    """implements a circle, gets area and perimeter"""
    import math

    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")

        else:
            self.__radius = radius

    def area(self):
        """calcs the area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calcs the perimeter of a circle"""
        return 2 * math.pi * self.__radius
