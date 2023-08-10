#!/usr/bin/python3
from sys import argv
argc = len(argv)

if argc == 1:
    print("0 arguments.")

else:
    str = "argument"
    str += "s:" if argc > 2 else ":"
    print("{} {}".format(argc - 1, str))
    for ag in range(1, argc):
        print("{}: {}".format(ag, argv[ag]))
