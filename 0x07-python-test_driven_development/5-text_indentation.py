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

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
