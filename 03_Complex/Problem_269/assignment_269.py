'''
Write a Python Program to create a list in which user 
perform all CRUD operations, user press number and it 
should work.

For 1 Display all item 
For 2 Insert a item
For 3 Update a item
For 4 Delete a item
'''
my_list = []

def display_items():
    if not my_list:
        print("The list is empty.")
    else:
        print("Items in the list:")
        for index, item in enumerate(my_list):
            print(f"{index + 1}. {item}")

def insert_item():
    item = input("Enter the item to insert: ")
    my_list.append(item)
    print(f"{item} has been added to the list.")

def update_item():
    display_items()
    if my_list:
        index = int(input("Enter the index of the item to update: ")) - 1
        if 0 <= index < len(my_list):
            new_item = input("Enter the new item: ")
            my_list[index] = new_item
            print("Item updated successfully.")
        else:
            print("Invalid index.")

def delete_item():
    display_items()
    if my_list:
        index = int(input("Enter the index of the item to delete: ")) - 1
        if 0 <= index < len(my_list):
            deleted_item = my_list.pop(index)
            print(f"{deleted_item} has been deleted.")
        else:
            print("Invalid index.")

while True:
    print("\nMenu:")
    print("1. Display all items")
    print("2. Insert an item")
    print("3. Update an item")
    print("4. Delete an item")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_items()
    elif choice == '2':
        insert_item()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
