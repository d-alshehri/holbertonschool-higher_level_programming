#!/usr/bin/python3
"""This module defines the Student class for JSON serialization."""


class Student:
    """Defines a student by first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of the student"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        return self.__dict__
