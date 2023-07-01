'''
Write A Python Program To Generate Number From 0 To 20 
Only Even Number And  Generate 0 To 20 Odd Number. 
Add Both Generated Number To Each Other To Display Total Result 
'''
# to gen even, 0 to 20
# add even
# to gen odd, 0 to 20
# add odd 
# add even + oddd

def Even_nums():
    s1 = 0
    print("\nEven Nums [0-20]")
    for i in range(0,21):
        if (i%2 == 0):
            s1 += i
            print(i)
    return s1

def Odd_nums():
    s2 = 0
    print("\nOdd nums [0-20]")
    for i in range(0,21):
        if (i%2 != 0):
            s2 += i
            print(i)
    return s2

if __name__=="__main__":
    total_even = Even_nums()
    total_odd = Odd_nums()
    print("\n")
    print("Even number = ", total_even)
    print("Odd number = ", total_odd)
    print("Total result is = "+str(total_even+total_odd))       