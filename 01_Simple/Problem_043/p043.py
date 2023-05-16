'''
Write A Python Program To Get Starting Number 
And Ending Number From The User To Display 
That Number With Proper Sequence

As, User Input 5 As Starting Number 
And 10 As A Ending Number, 
Then It Should Display
5, 6, 7, 8, 9,10
'''
# to get starting no
# to get ending no
# generate no from starting to ending

def display_numbers(s,e):
    for i in range(s, e+1): 
        print(i)

if __name__=="__main__":
    s = int(input("Enter a starting number: "))
    e = int(input("Enter a ending number : "))
    display_numbers(s,e)