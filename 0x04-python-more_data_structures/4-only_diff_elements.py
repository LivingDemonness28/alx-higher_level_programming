#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set_1.intersection(set_2)
    combined = set_1.union(set_2)
    not_union = combined.difference(common)
    return(not_union)
