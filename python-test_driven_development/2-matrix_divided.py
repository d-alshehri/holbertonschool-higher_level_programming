#!/usr/bin/python3
"""Provides a function to divide all elements of a matrix by a number."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The number that divide all elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not all the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with each element divided by div,
                       rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
