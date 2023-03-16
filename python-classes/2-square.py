#!/usr/bin/python3
"""A class that defines a square object by it's size."""


class Square:
    def __init__(self, size=0):
        """Initialize the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
            self.__size = size
