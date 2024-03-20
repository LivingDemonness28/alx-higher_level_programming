#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import *

    a = 10
    b = 5
    res = add(a, b)
    res1 = sub(a, b)
    res2 = mul(a, b)
    res3 = div(a, b)
    print("{} + {} = {}".format(a, b, res))
    print("{} - {} = {}".format(a, b, res1))
    print("{} * {} = {}".format(a, b, res2))
    print("{} / {} = {}".format(a, b, res3))
