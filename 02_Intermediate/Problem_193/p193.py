'''
Write a Python Program To find array size in bytes.
'''

from array import *

ar = array('i',[1,2,3,13,4,5,6,7])
print(ar)
one_item_size = ar.itemsize
# print(one_item_size)
total_len = len(ar)
total_size = total_len * one_item_size
print(str(total_size)+ " Byte")
