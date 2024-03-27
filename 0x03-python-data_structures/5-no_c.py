#!/usr/bin/python3
def no_c(my_string):
    new_chars = [char for char in my_string if char not in ('c', 'C')]
    new_string = ''.join(new_chars)
    return (new_string)
