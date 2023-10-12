'''
Write a Python Program to make dictionary to a text file
'''
myfile = open("filedict.txt","w")
dict = {1:"red",2:"blue",3:"yellow",4:"white"}

for k,v in dict.items():
    myfile.write(str(k))
    myfile.write(str(v))

myfile.close()