#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""


class LockedClass:
    """Presents first name."""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError("LockedClass object has no attribute 'last_name'")
            object.__setattr__(self, name, value)
