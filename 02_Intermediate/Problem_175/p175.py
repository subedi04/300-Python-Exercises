'''
Write a Python Program to get 10 number from user 
to store in a list. Make one number of all 10 number. 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> 2345678910
'''

if __name__=="__main__":
    lst = []
    for i in range(10):
        item = input("Enter number : ")
        lst.append(item)

    print(lst)
    one_num = "".join(lst)
    print(one_num)