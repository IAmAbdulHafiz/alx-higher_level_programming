#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divResult = a / b
    except (TypeError, ZeroDivisionError):
        divResult = None
    finally:
        print("Inside result: {}".format(divResult))
    return (divResult)
