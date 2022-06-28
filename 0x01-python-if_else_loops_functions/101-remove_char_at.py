#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        return str[:n] + str[n - len(str) + 1:]
    else:
        return str
