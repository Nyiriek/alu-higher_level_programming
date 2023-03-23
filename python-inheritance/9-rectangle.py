#!/usr/bin/python3

"""Class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize new rectangle.
        Args:
            width (int): Width of new rectangle
            height (int): Height of new rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns rectangle description."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
