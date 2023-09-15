'''
Write A Python Program To Generate OTP On User Request
'''
import string
import random

user_r = input("Would you like to generate OTP or not? y/n : ")

if user_r == 'y':
    length = int(input("Enter a lenght : "))
    l = length
    result = "".join(random.choices(string.digits + string.ascii_uppercase, k=l))
    print(result)
else:
    print("Okay, don't worry")