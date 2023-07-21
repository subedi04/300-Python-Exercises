'''
Write a Python program to get 5 number 
from user to store in a list.  Add all 
that number to each other using 
list comprehension.
'''

def get_numbers():
    numbers = []
    for i in range(5):
        try:
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return get_numbers()
    return numbers

def main():
    numbers_list = get_numbers()
    sum_of_numbers = sum([num for num in numbers_list])
    print(f"The sum of the numbers is: {sum_of_numbers}")

if __name__ == "__main__":
    main()
