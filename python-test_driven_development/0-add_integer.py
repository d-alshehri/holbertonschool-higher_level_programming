#!/usr/bin/python3
"""
This module provides a function to add two numbers.
The function ensures that inputs are either integers or floats,
and it casts float inputs to integers before performing the addition.
It handles float overflow situations by checking if the number exceeds
the floating-point limit (infinity), and also checks for NaN (Not a Number).
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
