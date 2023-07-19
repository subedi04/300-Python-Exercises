'''
Write a Python program to count any item from a nested list.
'''

if __name__=="__main__":
    n_list = [[1,2,3,4],[3,3,4,12]]
    print(n_list)
    item = int(input("Enter a list item : ")) # '2'> 2
    reuslt = sum(i.count(item) for i in n_list)
    print(reuslt)
