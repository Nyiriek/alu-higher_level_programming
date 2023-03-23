#!/usr/bin/python3
"""A class MyInt that inherits from int."""


class MyInt(int):
    """Inherits from int."""

    def __eq__(self, value):
        """Overides operator == and !=."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Magic method not equals."""
        return super().__eq__(value)
