#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    add = 0

    for i in range(0, len(unique_list)):
        add = add + unique_list[i]
    return (add)
