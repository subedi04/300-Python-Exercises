'''
Write a Python program to get a number 
from user to display sin and cos value 
of its previous number and next number.
'''

import math

if __name__=="__main__":
    number = float(input("Enter a number: "))

    previous_number = number - 1
    next_number = number + 1

    previous_sin = math.sin(previous_number)
    previous_cos = math.cos(previous_number)
    next_sin = math.sin(next_number)
    next_cos = math.cos(next_number)

    print(f"The sine of the previous number ({previous_number}) is: {previous_sin}")
    print(f"The cosine of the previous number ({previous_number}) is: {previous_cos}")
    print(f"The sine of the next number ({next_number}) is: {next_sin}")
    print(f"The cosine of the next number ({next_number}) is: {next_cos}")
