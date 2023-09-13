#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write string to a UTF8 text file.

    Args:
        filename (str): Name of file to write.
        text (str): Text to write to the file.
    
    Returns:
        Num of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
