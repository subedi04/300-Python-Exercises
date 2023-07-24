'''
Write a Python Program to Display set of element from a list.
'''

def display_unique_elements(input_list):
    unique_elements = set(input_list)
    print("Unique elements from the list:")
    for element in unique_elements:
        print(element)

if __name__ == "__main__":
    try:
        input_list = input("Enter elements of the list separated by spaces: ").split()
        display_unique_elements(input_list)
    except ValueError:
        print("Invalid input! Please enter elements separated by spaces.")
