#!/usr/bin/python3
'''Read file'''


def read_file(filename=""):
    '''reads a text file and prints it to stdout'''
    with open(filename, 'r', encoding='UTF8') as my_file:
        data = my_file.read()
        print(data, end="")


"""
read_file("my_file_0.txt")
"""
