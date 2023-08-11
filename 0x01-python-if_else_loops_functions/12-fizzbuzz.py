#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while (i < 101):
        if (i % 3 == 0 and i % 5 == 0):
            return ("FizzBuzz ")
        elif (i % 3 == 0):
            return ("Fizz ")
        elif (i % 5 == 0):
            return ("Buzz ")
        else:
            return (f"{i} ")
    i = i + 1
