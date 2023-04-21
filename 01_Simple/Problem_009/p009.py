# to make a table of user entered number


# 1 * 2 = 2
# 2 * 2 = 4
def table(num):
    for i in range(1,11):
        print(str(i)+" * "+str(num)+" = "+str(i*num))


if __name__=="__main__": 
    num = int(input("Enter a number : ")) 
    print("You entered : "+str(num)+"") 
    table(num)