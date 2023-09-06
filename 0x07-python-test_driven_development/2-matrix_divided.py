#!/usr/bin/python3
"""Define integer addition function"""


def matrix_divided(matrix, div):
    """Return int addition of a and b
    
    Float arguments typecasted to integer before addition.

    Raises:
        TypeError: matrix contain a val that isn't an int or float.
        TypeError: If matrix contains different row sizes.
        TypeError: If div not an int or float.
        ZeroDivisionError: If div is 0.
    """
    if (any(len(row) != len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if ((not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if ((not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
            matrix[i][j] = int(matrix[i][j])
            matrix[i][j] = round(matrix[i][j]/div, 2)
    
    return (matrix)
