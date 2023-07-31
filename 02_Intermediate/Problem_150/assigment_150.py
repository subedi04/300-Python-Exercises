'''
Write a Python Program to Create list from existed 
dictionary that count number less than 20 greater than 5
'''

def create_list(dictionary):
    count = 0
    for value in dictionary.values():
        if 5 < value < 20:
            count += 1
    return count

if __name__=="__main__":
    my_dict = {1: 10, 2: 25, 3: 15, 4: 30, 5: 5, 6: 18, 7: 8}
    my_list = create_list(my_dict)
    print(my_list)
