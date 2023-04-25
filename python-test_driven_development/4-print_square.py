#!/usr/bin/python3
"""Function that prints a square with a # characater"""


def print_square(size):
    """Presents a square with a # character"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
