'''
Write A Python Program To Read A Existing File 
And  Get Two Number From The User, Add them And 
Display Result To Existing File
'''

def add_numbers_to_file(file_name):
    try:
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Get two numbers from the user
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

            # Add the numbers
            result = num1 + num2

            # Write the result to the file
            file.write(f"The sum of {num1} and {num2} is: {result}\n")

        print("Result added to the file successfully.")
    except IOError:
        print(f"Error: Could not open the file {file_name}")


if __name__=="__main__":
    # Provide the file name or path
    file_name = "existing_file.txt"
    add_numbers_to_file(file_name)
