#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        from sys import exc_info, stderr
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return False
