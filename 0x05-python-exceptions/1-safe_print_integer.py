#!/usr/bin/python3


def safe_print_integer(value):
    """
    printing integer with the format
    "{:d}".format()
    """
    try:
        print("{:d}".format(value))
        print()
        return True
    except (TypeError, ValueError):
        return False
