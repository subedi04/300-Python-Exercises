'''
Write A Python Program To Generate Number 
From 1 To 100 With Properly 4 Number Difference. As 1 5 9 13 17 ….
'''

def Sequence_Four(s,e):
    for i in range(s,e+1,4):
        print(i)

if __name__=="__main__":
    s = int(input("Enter a starting number: "))
    e = int(input("Enter a ending number : "))
    Sequence_Four(s,e)