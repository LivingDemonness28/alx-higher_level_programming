#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file.

    Args:
        filename (str): The file to append to.
        text (str): String to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
