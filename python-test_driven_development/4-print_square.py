#!/usr/bin/python3
"""Defines a function that prints a square using the # character."""


def print_square(size):
    """Prints a square of the given size using the '#' character.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
