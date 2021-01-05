#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except:
        from sys import stderr, exc_info
        print("Exception: {}".format(exc_info()[1]), file=stderr)
