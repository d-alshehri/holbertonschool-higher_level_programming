#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class with private size attribute,
    validated on initialization,
    inherits area and __str__ from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square with size after validation.
        """
        self.integer_validator("size", size)
        # Call Rectangle __init__ with width and height equal to size
        super().__init__(size, size)
