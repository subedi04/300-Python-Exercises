'''
Write a Python Program to reverse a sub string from a string.
'''
from audioop import reverse

if __name__=="__main__":
    user_string = input("Enter a string : ")
    s = int(input("Enter a starting number : "))
    e = int(input("Enter a ending number : "))
    user_sub_s = user_string[s:e]
    print(user_sub_s)
    print(user_sub_s[::-1])
    print(user_string)