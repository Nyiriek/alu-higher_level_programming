#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""

class LockedClass:
    __slots__ = ['first_class']

    def __init__(self):
        """Init method."""
        pass
