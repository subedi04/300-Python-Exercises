'''
Write a Python Program to find addition of 
list element to create a new list. 
Add element of list as 1st and 2nd, 
2nd and 3rd, 3rd and 4th …
'''
lst = []

n = int(input("Enter a even number : "))
if n%2 != 0:
    print("Enter a even number")
else:
    for i in range(n):
        item = int(input("Enter a number : "))
        lst.append(item)
print(lst)

new_list = []
for i in range(n): # 6
    if i != n-1:
        item = lst[i] + lst[i+1]
        new_list.append(item)
print(new_list)