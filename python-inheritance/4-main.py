#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = true
if inherits_from(a, int):
    print("{} is inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} is inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} is inherited from class {}".format(a, object.__name__))
