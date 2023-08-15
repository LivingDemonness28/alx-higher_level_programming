#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)

    if idx < 0 or length <= idx:
        return (my_list)
    else:
        i = 0
        remove_list = []
        while (i < length):
            if i != idx:
                remove_list.append(my_list[i])
                i = i + 1
            else:
                i = i + 1
        my_list = remove_list
    
    return (my_list)
