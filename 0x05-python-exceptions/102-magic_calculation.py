#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1,3):
        try:
            if i > a:
                b = i ** a
                result += (a ** b) / i
        except BaseException:
            raise
import dis
dis.dis(magic_calculation)
