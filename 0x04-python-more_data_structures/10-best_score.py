#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0

    for i in a_dictionary:
        val = a_dictionary[i]
        if (val > max_val):
            max_val = val
    return (max_val)
