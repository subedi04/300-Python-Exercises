'''
Write A Python Program To Find 
Square Root Of Middle Element 
Of List Items
'''
import math

if __name__=="__main__":
    lst = [4,5,9,4,2]
    l = len(lst)
    print("Length of list = "+str(l))
    print("Items of List")
    
    for i in lst:
        print(i)

    half = l/2
    middle_el = int(half)
    sqrt_middle_el = math.sqrt(lst[middle_el])
    #print(middle_el) # 3
    print("Middle Element = "+str(lst[middle_el]))
    print("Square Root of Middle Element = " + str(sqrt_middle_el))
