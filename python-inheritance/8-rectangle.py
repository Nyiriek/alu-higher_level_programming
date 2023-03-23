#!/usr/bin/python3

"""A class that defines a rectangle from BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes instance."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
