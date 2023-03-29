#!/usr/bin/python3
"""Script that adds all arguments to a Python list."""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for i in range(1, argc):
    loadFile.append(sys.argv[i])
save_to_json_file(loadFile, "add_item.json")
