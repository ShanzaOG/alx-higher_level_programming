#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of the characters 'c' and 'C' from a string.
    Parameters:
    my_string: Input string
    Returns:
    my_string: The input string with all 'c' and 'C' characters removed.
    """
    result = ""
    for char in my_string:
        if char not in {'c', 'C'}:
            result += char
    return result
