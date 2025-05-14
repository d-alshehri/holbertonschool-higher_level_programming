#!/usr/bin/python3

    """
    This module provides a function to add two integers
    """
    def add_integer(a, b=98):
        """
        Adds two integers of floats after casting them to integers

        Args:
        a(int, float): First number.
        b(int, float, optional): Second number. Defaults to 98

        Returns:
        int: the sum of a and b after casting to intgers

        Raises:
        TypeError: if a or b is not an int or float
        """
        if not isinstance (a(int, float)):
            raise TypeError("a must be an integer")

        if not isinstance (b(int, float)):
            raise TypeError("b must be an integer")    
        
        return (int)a + (int)b
