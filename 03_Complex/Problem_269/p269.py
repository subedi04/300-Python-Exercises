'''
Write a Python Program to create a list in which user 
perform different operations, 
user press number and it should work.
For 1 Display all item 
For 2 Insert a item
For 3 Update a item
'''

lst = [1,3,4,6,12,53]

print("1 for dispalying")
print("2 for inserting item")
print("3 for Updating item")
num = int(input("Enter a number betwen 1 to 3 : "))

if num == 1:
    print("All the list items "+str(lst))

elif num == 2:
    item = int(input("Enter a list item : "))
    ind = int(input("Enter a list item index : "))
    lst.insert(ind, item)
    print("All the list items "+str(lst))

elif num == 3:
    upd_item = int(input("Enter a list updated item : "))
    up_ind = int(input("Enter a list item index : "))
    lst[up_ind] = upd_item
    print("All the list items "+str(lst))
else:
    print("Enter a number between 1 to 3")