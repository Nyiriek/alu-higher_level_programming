#!/usr/bin/python3

"""Function that returns True/False."""


def inherits_from(obj, a_class):
    """Returns True/False."""

    if not isinstance(obj, a_class):
        return True
    else:
        return False
