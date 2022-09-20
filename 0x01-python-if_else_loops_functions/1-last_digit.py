#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number_index = abs(number) % 10
if (number_index > 5):
    print(f"Last digit of {number} is {number_index} and is greater than 5")
elif (number_index == 0):
    print(f"Last digit of {number} is {number_index} and 0")
elif (number_index < 6) and (number_index != 0):
    print(f"Last digit of {number} is {number_index} and is less than 6 and not 0")
