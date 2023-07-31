'''
Write a Python Program Create dictionary 
from list that display its square as key
'''

def create_dict(lst):
    dictionary = {}
    for num in lst:
        dictionary[num**2] = num
    return dictionary

if __name__=="__main__":
    my_list = [1, 2, 3, 4, 5]
    my_dict = create_dict(my_list)
    print(my_dict)
