#!/usr/bin/python3
class Square:
    '''Definiation of a Square with private att size'''

    def __init__(self, size):
        '''initializes a square by size
           att: size
        '''
        self.__size = size


"""
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
"""
