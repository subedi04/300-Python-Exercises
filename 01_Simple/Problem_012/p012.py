'''
Write a Python program to display following output using for loop 
*
*  * 
* * *
* * * * 
* * * * *
'''

def pattern(n):
    for i in range(n+1):
        print("* "*i,end="\n")

if __name__=="__main__":
    n = int(input("Enter a number : "))
    pattern(n)