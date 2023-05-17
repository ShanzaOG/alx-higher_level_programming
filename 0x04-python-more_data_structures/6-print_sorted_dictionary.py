#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    sortinf a dictionary
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
