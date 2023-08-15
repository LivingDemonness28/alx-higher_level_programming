#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ('None')
    else:
        max_val = my_list[0]
        i = 0
        while (i < len(my_list)):
            if my_list[i] > max_val:
                max_val = my_list[i]
            i = i + 1
        return (max_val)
