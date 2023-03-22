#!/usr/bin/python3

"""A class that avoids dynamically created attributes."""


class LockedClass:
     """
    Avoid the user from giving new lockedclass attributes
    for anything ut only for the one called 'first_name'.
    """

    __slots__ = ["first_name"]
