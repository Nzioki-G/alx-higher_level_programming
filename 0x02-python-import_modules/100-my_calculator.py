#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[1])
    b = int(args[3])
    op = args[2]
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "/":
        res = div(a, b)
    else:
        res = mul(a, b)

    print("{} {} {} = {}".format(a, op, b, res))
