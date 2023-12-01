#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    totalNumber = 0
    for i in range(len(sys.argv) - 1):
        totalNumber += int(sys.argv[i + 1])
    print("{}".format(totalNumber))

# Abdu-Hafiz Yussif <abdulhafiz.yussif@aiesec.net>
