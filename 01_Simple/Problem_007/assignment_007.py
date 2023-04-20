'''
Write A Python Program To Calculate Intersection Of Three Set
A = {5,2,4,6,7,1} B = {5,3,11}, C = {4,5,12,2,1,0}
'''

A = {5,2,4,6,7,1} 
B = {5,3,11}
C = {4,5,12,2,1,0}

i1 = A.intersection(B)
i2 = i1.intersection(C)

print(i2)
