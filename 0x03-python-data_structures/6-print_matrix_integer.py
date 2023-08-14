#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for row in matrix:
          format_row = " ".join("{:2}".format(item) for item in row)
          print(format_row)
