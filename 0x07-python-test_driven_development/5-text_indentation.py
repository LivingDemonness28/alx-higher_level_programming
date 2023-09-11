#!/usr/bin/python3
"""Defines a new line indentation function"""


def text_indentation(text):
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    
    common_del = '|'
    for delim in ['.', '?', ':']:
        text = text.replace(delim, common_del)
    
    res_arr = text.split(common_del)

    i = 0

    while(i < len(res_arr)):
        print(res_arr[i].strip())
        print("\n")
        i = i + 1
