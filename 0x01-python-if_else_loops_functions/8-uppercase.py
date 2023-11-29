#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - ord('a') + ord('A')), end='')
        else:
            print(char, end='')
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

