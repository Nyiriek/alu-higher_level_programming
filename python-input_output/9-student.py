#!/usr/bin/python3
"""A class Student that defines a student."""


class Student:
    """Presents student data."""
    def __init__(self, first_name, last_name, age):
        """Initialize new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict. description of student data."""
        return (self.__dict__)
