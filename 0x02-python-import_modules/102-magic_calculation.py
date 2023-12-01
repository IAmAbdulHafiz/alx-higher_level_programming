#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        cal = add(a, b)
        for i in range(4, 6):
            cal = add(cal, i)
        return (cal)
    else:
        return(sub(a, b))
