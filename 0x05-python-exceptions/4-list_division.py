#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            res_list.append(division)
    return (res_list)
