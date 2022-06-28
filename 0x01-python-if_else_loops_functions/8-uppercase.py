#!/usr/bin/python3
def uppercase(str):
    new_str = ""

    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 123:
            ch = chr(ord(ch) - 32)
        new_str = new_str + ch
    print("{}".format(new_str))
