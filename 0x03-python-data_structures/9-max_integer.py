#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    _max = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > _max:
            _max = my_list[index]
    return (_max)
