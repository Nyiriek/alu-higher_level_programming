#!/usr/bin/python3
"""Function that returns JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Returns the JSON format of my_obj."""

    return json.dumps(my_obj)
