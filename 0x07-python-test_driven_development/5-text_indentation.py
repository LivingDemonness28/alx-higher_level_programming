#!/usr/bin/python3
"""Defines a new line indentation function"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'

    Args:
        text (str): Input string

    Raises:
        TypeError: If text type is not string.
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    
    common_del = '|'
    for delim in ['.', '?', ':']:
        text = text.replace(delim, common_del)
    
    res_arr = text.split(common_del)

    i = 0

    while(i < len(res_arr)):
        if (i < (len(res_arr)-1)):
            print(res_arr[i].strip())
            print("")
        if (i == (len(res_arr) - 1)):
            print(res_arr[i].strip())
        i = i + 1
