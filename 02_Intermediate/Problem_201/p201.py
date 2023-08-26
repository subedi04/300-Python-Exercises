'''
Write a Python Program to find average of 5 number.
'''

sum = 0
for i in range(5):
    n = int(input("Enter a number : "))
    sum += n
    
print("Total ="+str(sum))
ave = sum/5
print("Average ="+str(ave))

