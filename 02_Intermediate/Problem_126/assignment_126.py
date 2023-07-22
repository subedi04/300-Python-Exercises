'''
Write a Python program to filter Even numbers 
from a given dictionary keys. Display only 
those Value item which have even number. 
'''

def filter_even_numbers(dictionary):
    even_numbers = {}

    for key in dictionary:
        if key % 2 == 0:
            even_numbers[key] = dictionary[key]

    return even_numbers


if __name__=="__main__":
    example_dict = {
        1: 11,
        2: 22,
        3: 33,
        4: 44,
        5: 55,
        6: 66,
        7: 77
    }

    filtered_dict = filter_even_numbers(example_dict)

    print("Original Dictionary:", example_dict)
    print("Filtered Dictionary (Keys with even numbers):", filtered_dict)
