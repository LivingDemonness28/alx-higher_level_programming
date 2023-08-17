#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or not a_dictionary):
        return ('None')

    max_value = max(a_dictionary.values())
    max_keys = [key for key, value in a_dictionary.items() if value == max_value]
    if (1 < len(max_keys)):
        return ('None')
    else:
        return (max_keys[0])
