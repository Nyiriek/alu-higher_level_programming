#!/usr/bin/python3

"""Function that returns True/False."""


def inherits_from(obj, a_class):
    """Returns True/False."""

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
