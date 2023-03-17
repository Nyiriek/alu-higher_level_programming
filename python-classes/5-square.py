#!/usr/bin/python3

"""Define class square"""


class Square:
    """Present a Square"""

    def __init__(self, size=0):
        """Initialize the new square
        Args:
            size (int): Size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns the current square area"""
            return (self.__size ** 2)

        @property
        def size(self):
            """Returns the size value"""
            return (self.__size)

        @size.setter
        def size(self, value):
            """Sets the size of the new square"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be > 0")
            self.__size = value

        def my_print(self):
            """Prints a # square according to the size value"""
            if not self.__size:
                print()
            else:
                for i in range(self.__size):
                    for n in range(self.__size):
                        print("#", end='')
                    print()
