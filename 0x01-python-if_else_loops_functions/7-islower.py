#!/usr/bin/python3

def islower(c):
    return 'a' <= c <= 'z'

if __name__ == "__main__":
    islower_test_cases = ["a", "H", "A", "3", "g"]
    for char in islower_test_cases:
        print("{} is {}".format(char, "lower" if islower(char) else "upper"))
