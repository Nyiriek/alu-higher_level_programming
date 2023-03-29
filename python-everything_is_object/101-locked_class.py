#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""


class LockedClass:
    """Presents a locked class."""

    def __init__(self):
        self.first_name = None

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        self.__dict__[name] = value
        __slots__ = ["first_name"]
