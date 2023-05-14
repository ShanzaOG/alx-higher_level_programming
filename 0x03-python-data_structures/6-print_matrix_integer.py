#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Parameters:
    matrix (list of list of int): The input matrix.

    Returns:
    None
    """
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:3d}".format(num), end=" ")
            else:
                print("{:3d}".format(num))
