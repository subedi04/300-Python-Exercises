'''
Write a Python Program to Create a dictionary 
from list that display its square as value.
'''

if __name__=="__main__":
    list = [1,2,3,0,4,5,6]
    dic = {i:i*i for i in list}
    print(dic)