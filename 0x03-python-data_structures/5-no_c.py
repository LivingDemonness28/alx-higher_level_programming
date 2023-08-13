#!/usr/bin/python3
def no_c(my_string):
    split_str = my_string.split('')
    remove1 = 'c'
    remove2 = 'C'

    i = 0
    j = 0
    length = len(split_str)

    while (i < length):
        if remove1 in split_str:
            split_str.remove(remove1)
        i = i + 1

    while (j < length):
        if remove2 in split_str:
            split_str.remove(remove2)
        j = j + 1
    
    delim = ''
    my_string = delim.join(split_str)
    return (my_string)
