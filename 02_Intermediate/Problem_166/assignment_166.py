'''
Write a Python program to insert an element 
after each element of a list.
'''

def insert_after_each_element(input_list, element_to_insert):
    result_list = []
    for item in input_list:
        result_list.append(item)
        result_list.append(element_to_insert)
    return result_list

if __name__=="__main__":
    original_list = [1, 2, 3, 4, 5]
    element_to_insert = "X"
    modified_list = insert_after_each_element(original_list, element_to_insert)
    print(modified_list)
