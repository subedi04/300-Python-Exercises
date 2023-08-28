'''
Write A Python Program To Find Union , 
Intersection And Difference Of Two Set
'''
a = set()
b = set()

for i in range(5):
    a.add(int(input("Enter a element : ")))

for i in range(5):
    b.add(int(input("Enter b element : ")))


u = a.union(b)

print("Union of two set is  "+str(u))


i = a.intersection(b)
print("Intersection of two set is  "+str(i))


d = a.difference(b)
print("Difference of two set is  "+str(d))