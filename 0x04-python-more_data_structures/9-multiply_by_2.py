#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dict = a_dictionary
    for i in multi_dict:
        val = multi_dict[i]
        multi_dict[i] = 2*val
    return (multi_dict)
