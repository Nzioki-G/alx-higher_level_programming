#!/usr/bin/python3
for alpha in range(26, 0, -1):
    if alpha % 2 == 0:
        alpha += 96
    else:
        alpha += 64
    print("{}".format(chr(alpha)), end="")
