#!/usr/pbin/python3
'''A class that defines a square by it's size.'''


class Square:
    '''Present a square.'''
    def __init__(self, size=0):
        '''Method to initialize the square object.
        Args:
            size (int): Size of the new square.
        '''
        if not instance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
