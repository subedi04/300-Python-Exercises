'''
Write a Python program to get a number 
from user to display square of its
 previous number and next number.
'''

if __name__=="__main_":
    n = int(input("Enter a number : "))
    next_n = n + 1
    pre_n = n -1
    print("You entered "+str(n))
    print("Previous Number is "+str(pre_n)+ " And its square is "+str(pre_n*pre_n))
    print("Next Number is "+str(next_n)+ " And its square is "+str(next_n*next_n))