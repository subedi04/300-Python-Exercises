'''
Write a Python program to convert dictionary’s keys 
and values into two tuple. One tuple should store keys 
and other tuple should store values.
'''

def convert_dict_to_tuples(dictionary):
    keys_tuple = tuple(dictionary.keys())
    values_tuple = tuple(dictionary.values())
    return keys_tuple, values_tuple

if __name__=="__main__":

    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    keys_tuple, values_tuple = convert_dict_to_tuples(sample_dict)

    print("Keys tuple:", keys_tuple)
    print("Values tuple:", values_tuple)
