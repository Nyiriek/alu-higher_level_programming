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
        """Retrieves student dict. with filter conditions."""
        if attrs == None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp(elem) = self.__dict__[elem]
            return temp
