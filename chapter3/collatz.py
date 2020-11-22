#!/usr/bin/python3

import sys

def collatz(number):
    if number == 1:
        return 1
    if (number % 2) == 0:
        print(int(number / 2))
        return number / 2
    elif (number % 2) == 1:
        print (int(3 * number + 1))
        return 3 * number + 1

while True:
    try:
        user_input=int(input('Input number:\n'))
        result = collatz(user_input)
        while result !=1:
            result = collatz(result)
        
    except ValueError:
        print("You must enter integer!")
