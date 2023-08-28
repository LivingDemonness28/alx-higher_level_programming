#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = sum(1 for _ in my_list)
    while x < 0:
        a = input("Please enter a value for x: ")
        print(' ')
        try:
            x = int(a)
        except:
            print("Invalid input, please enter an integer")
            print(' ')
            continue
        if x < 0:
            print("Number must be 0 or higher")
            print(' ')
    res = ''.join(map(str, my_list[0 : x]))
    return(res)
