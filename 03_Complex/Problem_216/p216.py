'''
Write a Python Program to get
5 number from user, store in a list,
 convert to pandas series to change 
 their default index numbers to alpha. 
'''

import pandas as pd

if __name__=="__main__":
    lst = []

    for i in range(5):
        lst.append(int(input("Enter a number : ")))

    print("List Items "+str(lst))
    ps = pd.Series(lst)
    print("Pandas Items "+str(ps))
    ps_ = pd.Series(lst, index=['a','b','c','d','e'])
    print(ps_)

