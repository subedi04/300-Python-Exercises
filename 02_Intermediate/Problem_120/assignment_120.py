'''
Write a Python program to access element from a nested list.
'''


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing individual elements
print("Accessing individual elements:")
print("First element:", nested_list[0][0])  # Access the first element of the first sublist
print("Second element:", nested_list[1][1])  # Access the second element of the second sublist
print("Third element:", nested_list[2][2])  # Access the third element of the third sublist

# Accessing entire sublists using slicing
print("\nAccessing entire sublists:")
print("First sublist:", nested_list[0])
print("Second sublist:", nested_list[1])
print("Third sublist:", nested_list[2])
