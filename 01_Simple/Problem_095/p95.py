'''
Write Python Program To Get Number From User T
o Display Table In Reverse Order
Example:
2 * 10 = 20
2 * 09 = 18
And so on
'''
# to get a number
# find table, reverse order
if __name__=="__main__":
    num = int(input("Enter a number : ")) # 4

    for i in range(10,0,-1):
        print(str(num)+" * "+str(i) +" = "+str(num*i))

    # 4 * 10 = 40
    # 4 * 9 = 36
    