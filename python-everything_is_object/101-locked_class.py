#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""


class LockedClass:
    """Presents first name."""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError("Cannot add new attribute to LockedClass except 'first_name'")
            object.__setattr__(self, name, value)
