'''
Write Python Program to make use 
of isidigit method with string
'''

def check_all_digits(input_string):
    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is a digit using isidigit() method
        if not char.isidigit():
            return False
    return True

def main():
    # Get input from the user
    user_input = input("Enter a string: ")

    # Check if all characters in the input string are digits
    if check_all_digits(user_input):
        print("All characters in the string are digits.")
    else:
        print("Some characters in the string are not digits.")

if __name__ == "__main__":
    main()
