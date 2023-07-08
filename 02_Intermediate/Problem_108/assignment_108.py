'''
Write a Python Program To Find Total Length 
Of Values And Keys In a Dictionary
'''

def calculate_total_length(dictionary):
    total_length = 0
    for key, value in dictionary.items():
        total_length += len(str(key)) + len(str(value))
    return total_length

if __name__=="__main__":
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    total_length = calculate_total_length(my_dict)
    print("Total length:", total_length)
