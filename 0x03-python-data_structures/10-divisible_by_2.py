#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    i  = 0
    tof_list = []

    while (i < length):
        a = my_list[i] % 2
        if (a == 0):
            tof_list.append(True)
        elif (a == 1):
            tof_list.append(False)
        i += 1
    return (tof_list)
