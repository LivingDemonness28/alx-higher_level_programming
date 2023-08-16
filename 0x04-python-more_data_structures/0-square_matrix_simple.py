#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []

    for i in range(0, len(matrix)):
        row = []
        for j in range(0, len(matrix[i])):
            row.append(matrix[i][j]**2)
        square_matrix.append(row)

    return (square_matrix)
