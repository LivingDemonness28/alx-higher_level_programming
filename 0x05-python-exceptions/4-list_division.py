#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(0, list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                ele1 = my_list_1[i]
                ele2 = my_list_2[i]
                if (not isinstance(ele1, (int, float)) or not isinstance(ele2, (int, float))):
                    raise TypeError
                if ele2 == 0:
                    raise ZeroDivisionError
                division = ele1 / ele2
            else:
                raise IndexError
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
