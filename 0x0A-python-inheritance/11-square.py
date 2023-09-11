#!/usr/bin/python3
'''Square #2'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''

    def __init__(self, size):
        '''inits using parent's parent class'''
        Rectangle.__init__(self, size, size)

        self.__size = size

    def area(self):
        '''implements rectangular area for square'''
        return super().area()

    def __str__(self):
        return super().__str__()


"""
s = Square(13)

print(s)
print(s.area())
"""
