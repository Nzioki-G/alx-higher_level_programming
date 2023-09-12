#!/usr/bin/python3
'''write to file'''


def write_file(filename="", text=""):
    '''writes a string text to file'''
    with open(filename, 'w') as my_file:
        bytes = my_file.write(text)
    return bytes


"""
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
"""
