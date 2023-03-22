#!/usr/bin/python3

"""A class that inherits."""


class MyList(list):
    """Contains list."""

    def print_sorted(self):
        """Prints sorted list."""

        print(sorted(self))
