#!/usr/bin/python3
# This code writes a class that defines a square byt it's size
"""Define a class Square."""


class Square:
    """Presents a square."""

    def __init__(self, size=0):
        """Initialize the new square.
        Args:
            size (int): Size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

     def area(self):
         """Return the current area of the square."""
         return (self.__size * 2)
