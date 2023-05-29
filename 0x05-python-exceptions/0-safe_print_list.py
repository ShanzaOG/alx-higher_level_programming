#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Function that prints elements of a list
    """
    count = 0

    try:
        for element in my_list:
            print(element, end='')
            count += 1

            if count == x:
                break

    except TypeError:
        print("Error: Unable to print element.")

    finally:
        print()

    return count
