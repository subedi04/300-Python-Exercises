'''
Write a Python program to access multiple elements from a tuple. 
Starting index and ending index provided by user.
'''

def main():
    # Sample tuple (you can replace it with any other tuple)
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    
    start_index = int(input("Enter the starting index: "))
    end_index = int(input("Enter the ending index: "))

    # Check if the indices are within the valid range
    if start_index < 0 or end_index >= len(my_tuple) or start_index > end_index:
        print("Invalid indices provided.")
        return

    # Access the elements from the tuple and print the result
    selected_elements = my_tuple[start_index:end_index + 1]
    print("Selected elements from the tuple:", selected_elements)

if __name__ == "__main__":
    main()
