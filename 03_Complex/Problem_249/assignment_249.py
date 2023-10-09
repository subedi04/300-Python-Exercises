'''
Write a Python program to check whether password is strong or weak on WEB.
'''

import re

# Define a regular expression for strong passwords
strong_password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=.{8,})")


password = input("Enter your password: ")


if strong_password_regex.match(password):
    print("Your password is strong")
else:
    print("Your password is weak")

