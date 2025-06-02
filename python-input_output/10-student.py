#!/usr/bin/python3
"""
Defines a Student class with selective JSON serialization.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):

        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """
        Returns a dictionary representation of the instance.
        If attrs is a list of strings, only return those attributes.

        Args:
            attrs (list or None): List of attribute names to retrieve.

        Returns:
            dict: A dictionary of selected or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
