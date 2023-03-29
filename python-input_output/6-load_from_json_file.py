#!/usr/bin/python3
"""Function that creates an object from JSON file."""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file."""
    with open(filename) as readFile:
        return json.load(readFile)
