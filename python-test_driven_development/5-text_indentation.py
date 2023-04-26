#!/usr/bin/python3
"""Function that prints 2 new lines after .?: characters"""


def text_indentation(text):
    """Prints new lines after .?: characters
    Args:
        text: input string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for d in ".?:":
        text = (d + "\n\n").join(
            [line.strip(" ") for line in text.split(d)])

    print("{}".format(text, end="")
