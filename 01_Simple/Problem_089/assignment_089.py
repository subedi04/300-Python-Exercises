'''
Write A Python Program To Generate Number From 0 To 20 Only Divisible By 3 Number 
And  Generate 0 To 20 Only Divisible By 5. 
Add Both Generated Number To Each Other To Display Total Result
'''

def Nums_Divisible_Three():
    s1 = 0
    print("\nNums Divisible by Three [0-20]")
    for i in range(0,21):
        if (i%3 == 0):
            s1 += i
            print(i)
    return s1

def Nums_Divisible_Five():
    s2 = 0
    print("\nNums Divisible by Five [0-20]")
    for i in range(0,21):
        if (i%5 == 0):
            s2 += i
            print(i)
    return s2

if __name__=="__main__":
    total_nums_div_three = Nums_Divisible_Three()
    total_nums_div_five= Nums_Divisible_Five()
    print("\n")
    print("Sum of Total Nums Divisible by Three = ", total_nums_div_three)
    print("Sum of Total Nums Divisible by Five = ", total_nums_div_five)
    print("Total result is = "+str(total_nums_div_three+total_nums_div_five))       