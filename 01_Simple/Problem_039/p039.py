'''
Write A Python Program To Get 5 Number In The List, 
Pass That List In The Function To Multiply And Add That Number And Display Total Result.
'''
# to get 5 number from the user
# store in the list
# pass that list to the function 
# inside the function, find * and + 
# dispaly result to the user

def get_nums():
    lst = []

    for i in range(5): # 0 1 2 3 4
        lst.append(int(input("Enter a number to store in the list : ")))
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
    add_mul(lst)
    
    
    