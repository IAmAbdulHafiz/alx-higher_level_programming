#!/usr/bin/python3

def magic_calculation(a, b):
    my_result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                my_result += a ** b / i
        except:
            my_result = b + a
            break
    return (my_result)
