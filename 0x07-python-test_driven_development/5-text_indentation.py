#!/usr/bin/python3
"""Defines a new line indentation function"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'

    Args:
        text (str): Input string

    Raises:
        TypeError: If text type is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    newline = False

    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + '\n\n'
            newline = True
        elif char == ' ' and newline:
            continue
        else:
            new_text += char
            newline = False

    print(new_text)
