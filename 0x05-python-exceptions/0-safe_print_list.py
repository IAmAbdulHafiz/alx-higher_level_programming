#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    _return = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            _return += 1
        except IndexError:
            break
    print("")
    return (_return)
