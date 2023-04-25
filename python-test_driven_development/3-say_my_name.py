#!/usr/bin/python3
"""A function that prints say my name"""


def say_my_name(first_name, last_name=""):
    """Prints my name
    Args:
        first_name: First name
        last_name: Last name

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
