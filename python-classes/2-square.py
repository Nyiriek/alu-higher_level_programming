#!/usr/bin/python3
<<<<<<< HEAD

'''Define a class Square.'''


class Square:
    '''Present a square'''

    def __init__(self, size=0):
        '''Initialize the new square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueErroe("size must be >= 0")
        self.__size = size
=======
"""A class that defines a square object by it's size."""


class Square:
    def __init__(self, size=0):
        """Initialize the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
            self.__size = size
>>>>>>> 70a6e669ad4be1bdbbf4305065b4da3aea6b0cc4
