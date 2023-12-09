#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(_k, a_dictionary[_k])) for _k in sorted(a_dictionary)]
