#!/usr/bin/python3

"""Function that returns true otherwise false."""


def is_same_class(obj, a_class):
    """Returns true/false."""

    if type(obj) is a_class:
        return True
    else:
        return False
