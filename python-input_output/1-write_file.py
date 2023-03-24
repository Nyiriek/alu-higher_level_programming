#!/usr/bin/python3
"""This module contains a function that writes to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns\
            the number of characters written.
        Args:
            filename (str): Name of file to write to.
            text (str): String to write to the file.
        Returns:
                the number of characters written'
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
