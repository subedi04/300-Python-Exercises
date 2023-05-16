'''
Write A Python Program To Get Large Number As Starting 
And Lower Number As Ending Number, Display That Number 
From Large To Lower And Find Their Sum.
'''

def Display_Seq_Total(s,e):
    total_sum = 0

    print("The sequence is : ")
    for i in range(s,e+1):
        print(i)
        total_sum += i

    print("The sum of numbers is : ", total_sum)


if __name__=="__main__":
    s = int(input("Enter a starting no, that is larger : "))
    e = int(input("Enter a ending no that is lower: ")) 
    Display_Seq_Total(s,e)  
