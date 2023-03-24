#!/usr/bin/python3
"""This module defines a class Student."""


class Student:
    """Presents student data."""
    def __init__(self, first_name, last_name, age):
        """Initialize new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve student dict. representation.
        Present only attributes included in the list if attrs\
                is a list of strings.
        Args:
            attrs (list): Attributes to present(Optional).
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return (self.__dict__)
