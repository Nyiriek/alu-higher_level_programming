#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for n in range(len(matrix[i])):
            if n != 0:
                print(" ", end='')
            print("{}".format(matrix[i][n]), end='')
        print()
