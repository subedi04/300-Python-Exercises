'''
Write a Python Program to create a nested dictionary. 
And Also iterate nested dictionary items 
'''

def create_nested_dict():
    nested_dict = {}

    for i in range(3):  # Create three outer keys
        outer_key = input(f"Enter the outer key {i + 1}: ")
        nested_dict[outer_key] = {}
        for j in range(2):  # Create two inner keys for each outer key
            inner_key = input(f"Enter the inner key {j + 1} for {outer_key}: ")
            value = input(f"Enter the value for {outer_key} - {inner_key}: ")
            nested_dict[outer_key][inner_key] = value

    return nested_dict

def iterate_nested_dict(nested_dict):
    print("Iterating through the nested dictionary:")
    for outer_key, inner_dict in nested_dict.items():
        print(f"Outer Key: {outer_key}")
        for inner_key, value in inner_dict.items():
            print(f"Inner Key: {inner_key}, Value: {value}")
        print("-" * 30)

def main():
    nested_dict = create_nested_dict()
    iterate_nested_dict(nested_dict)

if __name__ == "__main__":
    main()
