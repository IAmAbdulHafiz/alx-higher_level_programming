#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(0, list_length):
        try:
            divResult = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divResult = 0
        except ZeroDivisionError:
            print("division by 0")
            divResult = 0
        except IndexError:
            print("out of range")
            divResult = 0
        finally:
            newList.append(divResult)
    return (newList)
