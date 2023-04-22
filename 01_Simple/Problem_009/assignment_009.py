'''
Write A Python Program To Get 2 Number From The User, And Display 2 Table For That Number.
'''

def Two_Tables(num1,num2):
    nums = [num1,num2]
    for i in range(0,2):
        print("\nTable for number : ", nums[i])
        for j in range(1,11):
            print(str(j)+" * "+str(nums[i])+" = "+str(j*nums[i]))




if __name__=="__main__":
    print("Please you must enter 2 numbers")
    print("The program generates two tables in base at your entered numbers")
    num1 = int(input(">>> Enter a number 1 : "))
    num2 = int(input(">>> Enter a number 2 : "))
    Two_Tables(num1,num2)