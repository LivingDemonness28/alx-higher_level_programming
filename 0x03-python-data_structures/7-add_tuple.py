#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    len1 = len(list_a)
    len2 = len(list_b)

    if len1 < 2:
        i = 0

        while (i < (2-len1)):
            list_a.append(0)
            i = i + 1
    
    if len2 < 2:
        j = 0

        while (i < (2-len2)):
            list_b.append(0)
            j = j + 1
    
    if (2 < len1):
        list_c = []

        list_c.append(list_a[0])
        list_c.append(list_a[1])

        list_a = list_c
    
    if (2 < len2):
        list_d = []

        list_d.append(list_b[0])
        list_d.append(list_b[1])

        list_b = list_d
    
    list_e = []
    k = 0

    while (k < 2):
        list_e.append((list_a[k] + list_b[k]))
        k = k + 1
    
    tuple_c = tuple(list_e)

    return (tuple_c)
