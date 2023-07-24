'''
Write a Python Program to get 10 number 
from user to print minimum, maximum and 
starting, ending number to user.
'''

def get_user_numbers():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        numbers.append(num)
    return numbers


if __name__ == "__main__":
    try:
        user_numbers = get_user_numbers()
        min_num = min(user_numbers)
        max_num = max(user_numbers)
        start_num = user_numbers[0]
        end_num = user_numbers[-1]

        print("\nResults:")
        print(f"Minimum number: {min_num}")
        print(f"Maximum number: {max_num}")
        print(f"Starting number: {start_num}")
        print(f"Ending number: {end_num}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
