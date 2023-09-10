#!/usr/bin/python3
"""
module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists - members can be of type ints or floats
        div: Number to be used for the division, either a float or an integer

    Raises:
        TypeError: If the matrix contains non-integers or non-floats
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0

    Returns:
        A new matrix which represents the result of the divs
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
