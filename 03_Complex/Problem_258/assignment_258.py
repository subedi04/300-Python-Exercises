'''
Write a Python Program to print the memory usage of List.
'''

import sys

my_list = [1, 2, 3, 4, 5]

# Calculate the memory usage of the list
memory_usage = sys.getsizeof(my_list)

# Print the memory usage in bytes
print(f"Memory usage of the list: {memory_usage} bytes")
