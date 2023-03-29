#!/usr/bin/python3
"""This module contains a function that reads from a file."""


def read_file(filename=""):
    """Presents function that reads from a file.
    Args:
        filename (str): Name of file to read from.
    Raises:
        Exception: when the file can be read
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
