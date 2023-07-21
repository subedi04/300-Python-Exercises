'''
Write a Python program to get 5 number 
from user to store in a list. Display 
all the numbers with power of 3 using 
list comprehension.
'''

if __name__=="__main__":
    lst = []
    for i in range(5):
        item = int(input("Enter a item : "))
        lst.append(item)
    print(lst)

    new_lst = [i*i*i for i in lst]
    print(new_lst)