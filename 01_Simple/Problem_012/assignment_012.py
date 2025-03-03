'''
Write a Python program to display following output using for loop 
*
* * 
* * *
* * * * 
* * * * *
'''

def pattern(n):
    for i in range(n+1):
        spaces = n-i
        print(" "*spaces + "*"*i)

if __name__=="__main__":
    n = int( 10)
    pattern(n) 