'''
Write a Python program to convert dictionary’s keys 
and values into two list. One list should store keys 
and other list should store values.
'''

if __name__=="__main__":
    d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
    print(d)
    
    key = []
    for i in d.keys():
        key.append(i)
    print(key)

    val = []
    for i in d.values():
        val.append(i)
    print(val)