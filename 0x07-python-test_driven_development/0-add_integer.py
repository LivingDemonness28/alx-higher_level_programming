#!/usr/bin/python3
"""Define integer addition function"""


def add_integer(a, b=98):
    """Return int addition of a and b
    
    Float arguments typecasted to integer before addition.

    Raises:
        TypeError: If a or b is neither int nor float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))
