#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to check for lowercase character using ASCII code
# demonstrates how to use a function and if condition to affect program output


def islower(c):
    """Checks for lowercase

    Args:
        c: a single character argument

    Returns:
        True: if c is lowercase
        False: if c is not lowercase
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
