'''
Write a Python Program To Get a Number From User, 
And Display Number From 0, Up To User Entered Number.
'''

def display_numbers_up_to_n(number):
    for i in range(number + 1):
        print(i)

# Get the number from the user
if __name__=="__main__":
    try:
        user_number = int(input("Enter a number: "))
        if user_number < 0:
            print("Please enter a non-negative number.")
        else:
            print("Numbers from 0 to", user_number, "are:")
            display_numbers_up_to_n(user_number)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
