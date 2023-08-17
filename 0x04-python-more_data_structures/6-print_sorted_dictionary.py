#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    i = 0

    while i < len(keys):
        key = keys[i]
        print("{:s}: {}".format(key, a_dictionary[key]))
        i += 1
