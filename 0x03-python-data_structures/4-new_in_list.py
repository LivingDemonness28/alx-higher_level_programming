#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()
    length = len(copied_list) - 1

    if idx < 0 or length < idx:
        return (copied_list)
    else:
        copied_list[idx] = element
        return (copied_list)
