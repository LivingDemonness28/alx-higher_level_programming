#!/usr/bin/python3
"""Define a square of '#' printing function"""


def print_square(size):
    """_summary_

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0
        TypeError: if size is a float and less than 0.
    """
    if (isinstance(size, int) and size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#"*size)
