'''
Write a Python program to get the total length 
of all values of a dictionary with string values. 
'''
def total_length_of_string_values(dictionary):
    total_length = 0
    for value in dictionary.values():
        if isinstance(value, str):
            total_length += len(value)
    return total_length

if __name__=="__main__":
    example_dict = {
        'key1': 'Hello',
        'key2': 'World',
        'key3': 'Python',
        'key4': 123,  # This value is not a string
        'key5': 'Programming',
    }

    total_length = total_length_of_string_values(example_dict)
    print("Total length of string values in the dictionary:", total_length)
