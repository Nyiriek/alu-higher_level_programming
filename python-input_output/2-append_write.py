#!/usr/bin/python3
"""This module contains a function that appends to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of the file and returns\
            the number of characters written.
    Args:
        filename (str): Name of file to append to'
        text (str): String to append to file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
