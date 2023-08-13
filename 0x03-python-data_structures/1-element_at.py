#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or length <= idx:
        print('None')
    else:
        print("{:d}".format(my_list[idx]))
