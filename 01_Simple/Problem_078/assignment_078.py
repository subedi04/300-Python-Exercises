'''
Write A Python Program To Get A Number 
From User To Return Its Next Number 
With Addition Of User Entered Number 
And Previous Number With Addition 
Of User Entered Number
'''

def get_next_number(n):
    next_number = n+1
    next_number += n
    previous_number = n-1
    previous_number += n
    return next_number, previous_number

if __name__=="__main__":
    # Get a number from the user
    number = int(input("Enter a number: "))

    # Calculate the next number with addition of the user-entered number 
    # 10
    # and the previous number with addition of the user-entered number
    next_number, previous_number = get_next_number(number)
    print(next_number,previous_number)

