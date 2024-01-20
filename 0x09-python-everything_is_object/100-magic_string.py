#!/usr/bin/python3
def magic_string():
    """
    Generates a string with "Holberton" based on function invocation count.
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string.n - 1) + "Holberton")
