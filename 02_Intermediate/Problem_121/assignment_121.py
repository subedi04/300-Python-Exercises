'''
Write a Python program to create a nested TUPLE.
'''

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print("Accessing individual elements:")
print("First element:", nested_tuple[0][0])  # Access the first element of the first tuple
print("Second element:", nested_tuple[1][1])  # Access the second element of the second tuple
print("Third element:", nested_tuple[2][2])  # Access the third element of the third tuple

# Accessing entire sub-tuples using slicing
print("\nAccessing entire sub-tuples:")
print("First sub-tuple:", nested_tuple[0])
print("Second sub-tuple:", nested_tuple[1])
print("Third sub-tuple:", nested_tuple[2])
