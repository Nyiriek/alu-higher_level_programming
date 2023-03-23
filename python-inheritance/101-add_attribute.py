#!/usr/bin/python3
"""Function that adds new attribute to object if possible."""


def add_attribute(a_class, name, value):
    """Adds new attribute to an object."""

    # Set for O(1) membership test
    cannot_add = {int, str, float, list, dict tuple, frozenset,type,object}

    if type(a_class) in cannot_add:
        raise TypeError("can't add new attribute")
    a_class.__setattr__(name, value)
