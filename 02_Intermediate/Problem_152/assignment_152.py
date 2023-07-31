'''
Write a Python Program to Create set that display only odd number
'''

def create_set(lst):
    odd_numbers = set()
    for num in lst:
        if num % 2 != 0:
            odd_numbers.add(num)
    return odd_numbers

if __name__=="__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_set = create_set(my_list)
    print(odd_set)
