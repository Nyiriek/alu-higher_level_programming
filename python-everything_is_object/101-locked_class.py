#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""


class LockedClass:
    """Presents first name."""
    def __init__(self):
        self.first_name = None

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"{name} attribute cannot be set on LockedClass")
        self.__dict__[name] = value
