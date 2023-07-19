'''
Write a Python program to access multiple elements from a list. 
'''
if __name__=="__main__":
    lst = [1,2,3,4,56,6,7,8,9,10]
    # print(lst[0:5]) # 0 1 2 3 4
    print(lst)
    s = int(input("Enter starting item position : ")) # 0
    e = int(input("Enter Ending item position : ")) #  5
    ending = e+1
    print(lst[s:ending])