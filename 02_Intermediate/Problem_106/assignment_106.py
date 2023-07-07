'''
Write A Python Program To Get Password From 
The User That Contain Alpha Numeric, Special Characters, 
And More Than 8 And Less Than 20 Characters And Restrict 
User If User Include Uppercase Letter And Space
'''

import re

def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    
    if not any(char.isupper() for char in password):
        return False

    if ' ' in password:
        return False

    if not re.match("^(?=.*[a-zA-Z0-9])(?=.*[@#$%^&+=])", password):
        return False
    
    return True

def get_password():
    while True:
        password = input("Enter your password: ")
        if validate_password(password):
            print("Password is valid.")
            break
        else:
            print("Invalid password. Please try again.")

if __name__=="__main__":
    get_password()
