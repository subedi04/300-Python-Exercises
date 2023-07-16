'''
Write A Python Program Sort Dictionary By Value
'''

def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    return sorted_dict

if __name__=="__main__":
    my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
    sorted_dict = sort_dict_by_value(my_dict)
    print(sorted_dict)
