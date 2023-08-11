#!/usr/bin/python3
def print_last_digit(number):
    dig = abs(number) % 10
    if number < 0:
        print(-1*dig)
    else:
        print(dig)