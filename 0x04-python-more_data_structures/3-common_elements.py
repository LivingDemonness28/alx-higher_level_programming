#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1, list_2, list_3 = list(set_1), list(set_2), []

    for i in range(0, len(list_1)):
        for j in range(0, len(list_2)):
            if (list_1[i] == list_2[j]):
                list_3.append(list_2[j])
    return(set(list_3))
