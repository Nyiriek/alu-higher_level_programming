#!/usr/bin/python3
"""Module that defines a class student."""


class Student:
    """Presents student data."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student data."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve student dict. presentation."""
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all student attributes."""
        for j, n in json.items():
            setattr(self, k, n)
