'''
Write a Python Program to update any key 
in a dictionary on user request.
'''

def update_key_in_dict(dictionary):
    print("Current Dictionary:", dictionary)
    key = input("Enter the key you want to update: ")

    if key in dictionary:
        new_value = input("Enter the new value for the key: ")
        dictionary[key] = new_value
        print("Key updated successfully!")
    else:
        print("Key not found in the dictionary. No update performed.")

    print("Updated Dictionary:", dictionary)


if __name__ == "__main__":
    my_dict = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer",
    }

    while True:
        print("\nMenu:")
        print("1. Update a key in the dictionary")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            update_key_in_dict(my_dict)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
