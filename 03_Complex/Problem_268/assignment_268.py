'''
Write a Python Program to create a list from existed 
list which display item without start and end char.
'''

existing_list = ['apple', 'banana', 'cherry', 'date']

# Create a new list by removing the first and last characters of each item
new_list = [item[1:-1] for item in existing_list]

# Display the new list
print(new_list)
