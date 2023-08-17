#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dict = {}
    for i in a_dictionary:
        val = a_dictionary[i]
        multi_dict[i] = a_dictionary[i]
        multi_dict[i] = 2*val
    return (multi_dict)
