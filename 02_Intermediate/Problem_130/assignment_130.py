'''
Write a Python program to find 
a maximum value in a dictionary 
(having value with number data type)
'''

def find_max_value(dictionary):
    if not dictionary:
        return None

    max_value = max(dictionary.values())
    return max_value

if __name__=="__main__":
    sample_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 5}
    max_value = find_max_value(sample_dict)

    if max_value is not None:
        print("Maximum value:", max_value)
    else:
        print("The dictionary is empty.")
