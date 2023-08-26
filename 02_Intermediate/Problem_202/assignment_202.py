'''
Write a Python Program to create a list on run time, 
display list element, and also find max and min item 
from list of integers using Procedural Programming.
'''

def create_list():
    try:
        n = int(input("Enter the number of elements in the list: "))
        num_list = []

        for i in range(n):
            num = int(input(f"Enter element {i + 1}: "))
            num_list.append(num)

        return num_list
    except ValueError:
        print("Invalid input. Please enter valid integers.")

def display_list(lst):
    print("List elements:")
    for num in lst:
        print(num, end=" ")
    print()

def find_max_min(lst):
    if not lst:
        print("The list is empty.")
        return

    max_num = max(lst)
    min_num = min(lst)
    
    print(f"Maximum element: {max_num}")
    print(f"Minimum element: {min_num}")

def main():
    num_list = create_list()
    if num_list:
        display_list(num_list)
        find_max_min(num_list)

if __name__ == "__main__":
    main()
