#!/usr/bin/python3

"""Class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle'). Rectangle


class Square(Rectangle):
    """Presents a square."""

    def __init__(self, size):
        """Initialize new square."""
        super().integer_validator("size", size)
        super().__int__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)
