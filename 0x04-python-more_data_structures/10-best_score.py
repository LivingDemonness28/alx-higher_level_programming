#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or not a_dictionary):
        return ('None')
    
    max_key = list(a_dictionary.keys())[0]
    max_val = a_dictionary[max_key]
    
    for key, value in a_dictionary.items():
        if (value > max_val):
            max_val = value
            max_key = key
    return (max_key)
