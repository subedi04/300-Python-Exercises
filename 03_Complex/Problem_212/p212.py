'''
Write a Python Program To Get 5 Items From A List 
And Display Items To User But Not Included Last, 
First Item And Odd Containing Length.
'''

lst = []

for i in range(5):
    lst.append(input("Enter a item : "))

for i in lst:
    if i != lst[0] and i != lst[-1] and len(i) != 5:
        print(i)