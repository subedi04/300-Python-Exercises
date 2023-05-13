'''
Write A Python Program To Get Two Number From The User , 
Pass To Function And Find Minimum
'''

def min_num(a, b):
    print("\nThis result is coming from the function")
    print("a = "+str(a))
    print("b = "+str(b))
    if(a < b):
        print("A is smaller")
    else:
        print("B is smaller")

if __name__=="__main__":
    x = int(input("Enter a number : "))
    y = int(input("Enter b number : "))
    min_num(x, y)