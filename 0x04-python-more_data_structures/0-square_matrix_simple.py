#!/usr/bin/Python3


def square_matrix_simple(matrix=[]):
    """
    Function that computes the square
    values of a matrix.
    """
    result = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)
        result.append(squared_row)

    return result
