'''
Create  a Python Program to Count total 
number of Uppercase , Lowercase and digits 
in a string. 
'''
def count_elements_in_string(s):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
            
    # Display the results
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Digits: {digit_count}")

if __name__=="__main__":
    input_string = input("Enter a string: ")
    count_elements_in_string(input_string)
