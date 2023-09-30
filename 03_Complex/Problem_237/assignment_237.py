'''
Write a Python Program to get a alpha character 
from user to check whether it is in given range 
or not: range(a to f) or (A-F)
'''

user_input = input("Enter a character: ")

# Check if the input character is in the specified range (a to f or A to F)
if user_input.isalpha() and len(user_input) == 1:
    char = user_input.lower()  # Convert the character to lowercase for comparison

    if 'a' <= char <= 'f':
        print(f"{user_input} is in the range (a to f)")
    elif 'A' <= char <= 'F':
        print(f"{user_input} is in the range (A to F)")
    else:
        print(f"{user_input} is not in the specified range.")
else:
    print("Please enter a single alphabetic character.")
