#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    i = 0

    while(i < list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                if b != 0:
                    res = a / b
                else:
                    print("division by 0")
                    res = 0
            else:
                print("wrong type")
                res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            res_list.append(res)
    return (res_list)
