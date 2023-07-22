'''
Write a Python program to print a dictionary items line 
by line. Key and value should have one tab distance.   
'''

if __name__=="__main__":

    d = {1:"Red",2:"Blue",3:"Yellow",4:"Black",5:"Green"}
    print(d)
    for k,v in d.items():
        print(str(k) +"\t"+str(v))