#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    _avg = 0
    _size = 0
    for _tup in my_list:
        _avg += (_tup[0] * _tup[1])
        _size += _tup[1]
    return (_avg / _size)
