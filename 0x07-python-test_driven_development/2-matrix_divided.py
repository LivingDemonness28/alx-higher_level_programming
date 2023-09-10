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
    Returns:
        A new matrix representing the result of the division.
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"
    msg3 = "division by zero"
    msg4 = "div must be a number"
    new_matrix = []

    if (matrix == []):
        raise TypeError(msg1)
    if (not all(isinstance(i, list) for i in matrix)):
        raise TypeError(msg1)
    if (not all((isinstance(k, int)) or (isinstance(k, float))
                for k in [num for i in matrix for num in i])):
        raise TypeError(msg1)
    if (any(len(row) != len(matrix[0]) for row in matrix)):
        raise TypeError(msg2)
    if (div == 0):
        raise ZeroDivisionError(msg3)
    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError(msg4)

    for i in range(0, len(matrix)):
        new_row = []
        for j in range(0, len(matrix[i])):
            new_row.append(round(matrix[i][j]/div, 2))
        new_matrix.append(new_row)

    return (new_matrix)
