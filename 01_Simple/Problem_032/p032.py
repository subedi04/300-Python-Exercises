'''
Write A Python Program To Get Two Number From The User , 
Pass To Function And Find Maximum
'''
# to get 2 number 
# pass to function 
# max



def max_num(a, b):
    print("\nThis result is coming from the function")
    print("a = "+str(a))
    print("b = "+str(b))
    if(a > b):
        print("A is greater")
    else:
        print("B is greater")

if __name__=="__main__":
    x = int(input("Enter a number : "))
    y = int(input("Enter b number : "))
    max_num(x, y)