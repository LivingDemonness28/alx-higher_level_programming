#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        i = 0
        length = len(my_list)
        while (i < length):
            print("{:d}".format(my_list[i]))
            i = i + 1
