#!/usr/bin/python3
"""Module for Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the Rectangle instance."""
        self.width = width
        self.height = height
        super().__init__()

    def __str__(self):
        """Return string representation of the Rectangle instance."""
        return ("Rectangle[] {}/{}".format(self.__wiiidth, self.__height))

    def area(self):
        """Return the area of the Rectangle instance."""
        return (self.__width * self.__height)
