#!/usr/bin/python3
def sqaure_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return(new_matrix)
