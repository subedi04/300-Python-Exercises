'''
Write A Python Program To Generate A Strong Password, 
Password Length Should Be Decided By User.
'''

import random
import string

def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


if __name__=="__main__":
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
