'''
Write A Python Program To Get a number from user and display 
table of that number in a file. And find product of all result 
that come from table.
'''

myfile = open("mytable.txt","w")

num = int(input("Enter a number : "))
product = 1
for i in range(1, 11):
    # 1 * 2 = 2 
    table  = str(i)+" * "+str(num)+" = "+str(i*num)
    myfile.write(str(table)+" \n")
    product *= i*num
print("Product = "+str(product))
myfile.write(str(product))
myfile.close()