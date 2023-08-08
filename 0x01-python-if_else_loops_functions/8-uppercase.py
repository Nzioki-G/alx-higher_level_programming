#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for character in str:
        asc = ord(character)
        if asc >= 97 and asc <= 122:
            character = chr(asc - 32)
        print("{}".format(character), end="")
    print()


'''
uppercase("best")
uppercase("Best School 98 Battery street")
'''
