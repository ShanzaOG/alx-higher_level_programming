#!/usr/bin/python3


def best_score(a_dictionary):
    """
    returns the key with the biggest
    integer value
    """
    val = 0
    big = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > val:
                val = value
                big = key
    return big
