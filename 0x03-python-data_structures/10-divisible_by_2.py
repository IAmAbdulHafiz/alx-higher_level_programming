#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multi_num = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            multi_num.append(True)
        else:
            multi_num.append(False)

    return (multi_num)
