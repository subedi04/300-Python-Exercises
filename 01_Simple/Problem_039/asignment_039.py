'''
Write A Python Program To Get 5 Number In The TUPLE, 
Pass That TUPLE In The Function To Multiply 
And Add That Number And Display Total Result. 
'''

def get_nums():
    lst = []

    for i in range(5): # 0 1 2 3 4
        lst.append(int(input("Enter a number to store in the list : ")))
    lst = tuple(lst)
    return lst
#print(lst)

def add_mul(lst_num):
    s = 0
    m =  1
    for i in lst_num:
        s += i
        m *= i  
    print("Addition = "+ str(s))
    print("Multiplicaiton = "+ str(m))

if __name__=="__main__":
    lst = get_nums()
    print(lst)
    add_mul(lst)