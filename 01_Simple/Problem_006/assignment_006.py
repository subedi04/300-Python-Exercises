'''
Write a Python Program to calculate union of Three set
A = {5,12,52,0,8} B = {2,5,1,9,8}, C = {4,5,6,0,10}
'''

A = {5,12,52,0,8}

B = {2,5,1,9,8}

C = {4,5,6,0,10}

u1 = A.union(B)
u2 = u1.union(C)

print(u2)
