#!/usr/bin/python3
"""Function that returns a list of lists of integers\
        representing the Pascal's triangle."""


def pascal_triangel(n):
    """Represents Pascal's triangle of size n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]

        for m in range(1, i):
        curr_row.append(prev_row[m-1] + prev_row[m])

        curr_row.append[1]
        triangle.append(curr_row)

    return triangle
