#!/usr/bin/python3
"""
Defines a Student class with JSON serialization.
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

    def to_json(self):

        """
        Returns the dictionary representation of the instance
        for JSON serialization.

        Returns:
            dict: A dictionary of instance attributes.
        """
        return self.__dict__
