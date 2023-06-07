'''
Write A Python Program To Find Minimum Number 
From A List Using Function 
'''

def min_num(l):
    #print(type(l))
    print("The min number is : ",min(l))

if __name__ == "__main__":
    lst = []

    for i in range(10):
        lst.append(int(input("Enter number : ")))
    #print(lst)
    min_num(lst)
