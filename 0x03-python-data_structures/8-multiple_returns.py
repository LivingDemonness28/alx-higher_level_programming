#!/usr/bin/python3
def multiple_returns(sentence):
    list1 = []
    length = len(sentence)
    if sentence == "":
        list1 = [length, 'None']
    else:
        list1 = [length, sentence[0]]
    
    tuple1 = tuple(list1)
    return (tuple1)
