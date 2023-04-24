#!/usr/bin/python3
"""A function that adds two numbers"""


def add_integer(a, b=98):
    """Returns the sum of two numbers.
    Args:
        a: first integer/float number
        b: second integer/float number with 98 as default
    
    Raises:
        TypeError if a or b are not integers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return (a + b)
