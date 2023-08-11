'''
Write a Python program to take Python data 
from user to convert into JSON Data.
'''

import json

def main():
    user_input = input("Enter a Python dictionary or list: ")

    try:
        python_data = eval(user_input)  # Safely evaluate the user input as Python code
        json_data = json.dumps(python_data, indent=4)
        print("JSON data:")
        print(json_data)
    except (SyntaxError, TypeError):
        print("Invalid input. Please enter a valid Python dictionary or list.")


if __name__ == "__main__":
    main()
