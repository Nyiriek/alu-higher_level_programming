#!/usr/bin/python3
"""Function that adds new attribute to object if possible."""


def add_attribute(obj, att, value):
    """Adds new attribute to an object.
    Args:
        obj (any): Object to add attribute to.
        att (str): Name of attribute to be added.
        value (any): Value of attribute.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
