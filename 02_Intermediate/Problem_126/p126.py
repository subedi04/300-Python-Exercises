'''
Write a Python program to filter odd numbers 
from a given dictionary keys. Display only 
those values which have odd keys.
'''

if __name__=="__main__":
    d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
    print(d)
    for k,v in d.items():
        if k%2 != 0:
            print(v)