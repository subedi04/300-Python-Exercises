'''
Write A Python Program To Remove First 
And Last Characters From A String
'''

s = input("Enter a sentence : ")
l = list(s)
del(l[0])
del(l[-1])
cad = "".join(l)
print(cad)