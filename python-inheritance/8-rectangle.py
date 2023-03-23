#!/usr/bin/python3

"""A rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Inherits."""

    def __init__(self, width, height):
        """Initialize method to inherit."""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height
