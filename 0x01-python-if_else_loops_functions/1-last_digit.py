#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number

if number < 0:
    number = -(number)

last_digit = number % 10

if temp < 0:
    number = temp
    last_digit = -(last_digit)

if last_digit > 5:
    print(f"Last digit of {temp} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print (f"Last digit of {temp} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print (f"Last digit of {temp} is {last_digit} and is less than 6 and not 0")
