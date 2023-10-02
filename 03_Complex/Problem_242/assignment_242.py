'''
Write a Python program to check a to z, A- Z, 
0 to 9 and _ from a user entered string at 
ENDING position.
'''

def check_ending_characters(string):
    ending_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    if string[-1] in ending_characters:
        return True
    else:
        return False

user_string = input("Enter a string: ")
if check_ending_characters(user_string):
    print("The string ends with a to z, A to Z, 0 to 9, or _")
else:
    print("The string does not end with a to z, A to Z, 0 to 9, or _")
