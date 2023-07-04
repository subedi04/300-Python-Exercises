'''
Write Python Program To Get Number From 
User To Display Table In Reverse Order. 
Number Should Multiply With Odd Number Only
'''

if __name__=="__main__":
    num = int(input("Enter a number : "))

    for i in range(9,0,-2):
        print(str(num)+" * "+str(i) +" = "+str(num*i))