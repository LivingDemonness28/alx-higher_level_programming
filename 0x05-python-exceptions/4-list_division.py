#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    i = 0

    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
        except (IndexError, TypeError):
            if ((i > len(my_list_1)) or (i > len(my_list_2))):
                print("out of range")
            else:
                print("wrong type")
            div = 0
        else:
            if (my_list_2[i] == 0):
                print("division by 0")
                div = 0
        finally:
            res_list.append(div)
        i += 1

    return (res_list)
