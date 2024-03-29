#!/usr/bin/python3
"""disassembles a circle class"""


import dis
import math


class MagicClass:
    """source code from bytecode"""

    def __init__(self, radius=0):
        '''inits a circle'''
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        '''calculates circle area'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''calculates circle perimeter'''
        return 2 * math.pi * self.__radius


# dis.dis(MagicClass)
