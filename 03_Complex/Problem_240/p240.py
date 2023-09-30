'''
Write a Python program to find the sequences of 
UPPERCASE and lowercase letters. Lowercase should 
be at end.
'''
import re

if __name__=="__main__":
    sent = input("Enter a sentence : ")

    x = re.search('^[A-Z+[a-z]+$', sent)

    if x:
        print("Matching....")
    else:
        print("Not Matching")