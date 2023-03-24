#!/usr/bin/python3
"""Function that returns an object represented by JSON string."""
import json


def from_json_string(my_str):
    """Returns an objected by a JSON string."""
    return json.loads(my_str)
