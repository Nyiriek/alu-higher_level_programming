#!/usr/bin/python3
"""Function that prints 2 new lines after .?: characterss"""


def text_indentation(text):
    """Prints new lines after .?: characters
    Args:
        text: input string
    """
    if type(text) != str:
        raise TypeError("text must be a srting")

    for d in in ".?:":
        text = (d + "\n\n").join(
            [line.strip(" ") for line in text.split(d)])

    print("{}".format(text, end="")
