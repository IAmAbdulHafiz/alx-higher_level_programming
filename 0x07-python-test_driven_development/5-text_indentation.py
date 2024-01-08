#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    my_char = 0
    while my_char < len(text) and text[my_char] == ' ':
        my_char += 1

    while my_char < len(text):
        print(text[my_char], end="")
        if text[my_char] == "\n" or text[my_char] in ".?:":
            if text[my_char] in ".?:":
                print("\n")
            my_char += 1
            while my_char < len(text) and text[my_char] == ' ':
                my_char += 1
            continue
        my_char += 1
