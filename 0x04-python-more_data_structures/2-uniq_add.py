#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_result = 0
    for x in set(my_list):
        my_result += x
    return (my_result)
