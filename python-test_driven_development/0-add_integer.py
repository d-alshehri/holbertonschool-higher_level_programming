#!/usr/bin/python3
"""
This module provides a function to add two numbers.

The function ensures that inputs are either integers or floats,
and it casts float inputs to integers before performing the addition.
It handles float overflow situations by checking if the number exceeds 
the floating-point limit (infinity), and also checks for NaN (Not a Number).
"""

import math

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
        OverflowError: If a or b is a floating-point number that overflows.
        ValueError: If a or b is NaN (Not a Number).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for NaN (Not a Number)
    if math.isnan(a):
        raise ValueError("a cannot be NaN")
    
    if math.isnan(b):
        raise ValueError("b cannot be NaN")

    # Check for float overflow (if a or b is infinity)
    if (isinstance(a, float) and (a == float('inf') or a == -float('inf'))) or \
       (isinstance(b, float) and (b == float('inf') or b == -float('inf'))):
        raise OverflowError("a or b has overflowed as a float")

    return int(a) + int(b)
