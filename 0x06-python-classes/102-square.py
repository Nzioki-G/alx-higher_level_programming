#!/usr/bin/python3
"""Last of Square"""


class Square:
    '''Square with methods for ==, !=, <, <=, >, >='''

    def __init__(self, size=0):
        '''initializes a square by size
        optional att: size'''
        self.size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter: retrieves the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: sets/updates the private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        '''compares 2 sqaures for equality in area'''
        return self.__size == other

    def __ne__(self, other):
        '''compares 2 squares for non-equality'''
        return self.__size != other

    def __gt__(self, other):
        '''comapares for greater than'''
        return self.__size > other

    def __ge__(self, other):
        '''compares for greater than or equality'''
        return self.__size >= other

    def __lt__(self, other):
        '''compares for less than area'''
        return self.__size < other

    def __le__(self, other):
        '''compares for less than or equality'''
        return self.__size <= other


"""
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")
"""
