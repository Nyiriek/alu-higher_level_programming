#!/usr/bin/python3

"""Function that returns True/False."""


def is_kind_of_class(obj, a_class):
    """Returns True/False."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
