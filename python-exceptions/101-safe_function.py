#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as c:
        sys.stderr.write("Exception: {}\n".format(c))
        result = None

    return (result)
