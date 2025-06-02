#!/usr/bin/python3
"""
12-pascal_triangle module

This module provides a function to generate Pascal's triangle of a given size.

Functions:
    pascal_triangle(n):
    Returns a list of lists representing Pascal's triangle with n rows.
"""


def pascal_triangle(n):

    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of n.

    If n <= 0, returns an empty list.

    Args:
        n (int): The number of rows of the Pascal's triangle to generate.

    Returns:
        list of lists:
        Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i - 1]
        # Compute the intermediate values of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
