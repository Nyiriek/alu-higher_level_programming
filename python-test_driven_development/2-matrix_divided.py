#!/usr/bin/python3
"""A function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides elements of a matrix
    Args:
        matrix: list of lists
        div: number that divides a matrix
    """

    if not isinstance(matrix, (list,)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    common_size = len(matrix[0])
    for row in matrix:
        if len(row) != common_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list())
        for k in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][k] / div, 2))
    return new_matrix
