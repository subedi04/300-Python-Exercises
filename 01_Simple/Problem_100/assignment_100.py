'''
Write A Python Program To Add Even Number From List
'''

if __name__=="__main__":
    even_lst = []
    for i in range(10):
        n = int(input("Enter even number : "))
        if n%2==0:
            even_lst.append(n)
    
    print(even_lst)