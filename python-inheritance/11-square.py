#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle,
with size validation and custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class with private size attribute,
    validates size,
    overrides __str__ to print [Square] <width>/<height>.
    """

    def __init__(self, size):
        """
        Initialize Square with size after validation.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
