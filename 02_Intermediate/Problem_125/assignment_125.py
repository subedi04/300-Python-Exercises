'''
Write a Python program to create a alpha string 
based dictionary to print dictionary items in uppercase. 
'''

import string
import random

def generate_alpha_string_dict():
    alpha_string = string.ascii_lowercase
    alpha_string_dict = {}

    for char in alpha_string:
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        alpha_string_dict[char] = random_string

    return alpha_string_dict

def print_dict_in_uppercase(dictionary):
    for key, value in dictionary.items():
        print(key.upper(), value.upper())

if __name__=="__main__":
    alpha_string_dict = generate_alpha_string_dict()
    print_dict_in_uppercase(alpha_string_dict)
