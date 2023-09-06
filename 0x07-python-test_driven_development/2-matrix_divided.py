#!/usr/bin/python3
"""Define integer addition function"""


def matrix_divided(matrix, div):
    """Return int addition of a and b
    
    Float arguments typecasted to integer before addition.

    Raises:
        TypeError: If matrix[i][j] or div is neither int nor float.
        ZeroDivisionError: If div is 0.
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    elif ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")

    i = 0
    length1 = len(matrix)
        
    while (i < length1):
        j = 0
        length2 = len(matrix[i])

        while (j < length2):
            if ((not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
             
            matrix[i][j] = int(matrix[i][j])
            matrix[i][j] = round(matrix[i][j]/div, 2)
            j = j + 1
        i = i + 1
    return (matrix)
