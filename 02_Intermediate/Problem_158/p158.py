'''
Write a Python Program to Display 
element of list with their occurrence
'''

lst = [1,1,2,2,3,4,5,1,5,6]
print(lst)
new_list = [str(i)+" have occerrences of "+str(lst.count(i)) for i in lst]
print(new_list)
for i in new_list:
    print(i)