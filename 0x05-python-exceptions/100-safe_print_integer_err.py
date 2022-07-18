#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
        return True
    except BaseException as error:
        print(f"Exception: {error}", file=sys.stderr)
        return False
