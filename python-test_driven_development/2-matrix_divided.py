#!/usr/bin/python3
"""A function that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides elements of a matrix
    Args:
        matrix: list of lists
        div: number that divides a matrix

    Raises:
        TypeError if:
            the elements of a matrix are not lists
            the elements of the lists aren't integers or floats
            div is not an integer or float
            lists of the matrix don't have the same size

        ZeroDivisionError if div is zero
    """

    if not isinstance(matrix, (lists)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    common_size = len(matrix[0])
    for row in matrix:
        if len(row) != common_size:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("divvision by zero")

        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append(list())
            for k in range(len(matrix[i])):
                new_matrix[i].append(round(matrix[i][k] / div, 2))
        return (new_matrix)
