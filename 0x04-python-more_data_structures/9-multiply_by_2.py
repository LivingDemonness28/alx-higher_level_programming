#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        val = a_dictionary[i]
        a_dictionary[i] = 2*val
    return (a_dictionary)
