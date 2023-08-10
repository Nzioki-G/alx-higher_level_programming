#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for idx in range(1, len(argv)):
        sum += int(argv[idx])
    print(sum)
