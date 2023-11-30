#!/usr/bin/python3

"""
A function that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    tri = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        row.append(1)
        tri.append(row)
    return tri
