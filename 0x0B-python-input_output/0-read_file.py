#!/usr/bin/python3
'''Read file'''


def read_file(filename=""):
    '''reads a text file and prints it to stdout'''
    with open(filename, 'r') as my_file:
        data = my_file.read()
        print(data)


"""
read_file("my_file_0.txt")
"""