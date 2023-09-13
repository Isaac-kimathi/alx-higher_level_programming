#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        row = triangles[-1]
        tmp = [1]
        for x in range(len(row) - 1):
            tmp.append(row[x] + row[x + 1])
            tmp.append(1)
            triangles.append(tmp)
    return triangles
