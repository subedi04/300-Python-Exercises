'''
Write a Python program to find the sequences of 
lowercase and UPPERCASE letters. Uppercase should 
be at end.
'''
import re


if __name__=="__main__":
    text = input("Enter a string: ")

    # Define a regular expression pattern
    pattern = r'[a-z]+[A-Z]+$'

    # Find all matches in the input string
    matches = re.findall(pattern, text)

    if matches:
        print("Sequences found:")
        for match in matches:
            print(match)
    else:
        print("No matching sequences found.")
