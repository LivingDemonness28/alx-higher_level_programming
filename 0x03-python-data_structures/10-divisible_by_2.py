#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tof_list = []

    for num in my_list:
        if (num % 2 == 0):
            tof_list.append(True)
        elif (num % 2 == 1):
            tof_list.append(False)
    return (tof_list)
