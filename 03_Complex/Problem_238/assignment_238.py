'''

Write a Python program to get a string from user that have starting 
char f and ending char z (zero, one or many z).  
Having between optional character also.
'''
import re


if __name__=="__main__":
    user_input = input("Enter a string: ")

    # Define the regular expression pattern
    pattern = r'^f.*z+$'

    # Check if the input string matches the pattern
    if re.match(pattern, user_input):
        print(f"'{user_input}' matches the pattern.")
    else:
        print(f"'{user_input}' does not match the pattern.")
