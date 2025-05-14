#!/usr/bin/python3
"""
This module provides a function to add two numbers.

The function ensures that inputs are either integers or floats,
and it casts float inputs to integers before performing the addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: The sum of a and b after casting to integers.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
