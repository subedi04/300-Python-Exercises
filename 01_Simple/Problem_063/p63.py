'''
Write A Python Program To Find Maximum Number 
From A List Using Function 
'''
# To ge 10 number, store in the list
# Pass to function
# find max number
def max_num(l):
    #print(type(l))
    print(max(l))

if __name__ == "__main__":
    lst = []

    for i in range(10):
        lst.append(int(input("Enter number : ")))
    #print(lst)
    max_num(lst)

