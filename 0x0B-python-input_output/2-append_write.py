#!/usr/bin/python3
'''Appends to file'''


def append_write(filename="", text=""):
    '''appends string at the end of file'''
    with open(filename, 'a') as my_file:
        bytes = my_file.write(text)
    return bytes


"""
nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
"""
