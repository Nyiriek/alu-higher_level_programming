#!/usr/bin/python3

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
