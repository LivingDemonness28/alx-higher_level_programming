#!/usr/bin/python3
"""Defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as rfile:
        for line in rfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wfile:
        wfile.write(text)
