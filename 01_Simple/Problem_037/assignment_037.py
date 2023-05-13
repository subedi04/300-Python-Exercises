'''
Write A Python Program To Get 6 Number From The User 
To Find The Square Of First Three Number 
And Find Cube Of Next Three Number
'''

def get_numbers():
    numbers = []

    for i in range(6):
        numbers.append(int(input("Enter your number : ")))
    return numbers

def Square_Cube(numbers):
    for i in range(0,len(numbers)-3):
        numbers[i] = pow(numbers[i],2)
    
    for j in range(3,len(numbers)):
        numbers[j] = pow(numbers[j],3)
    
    return numbers

if __name__=="__main__":
    numbers = get_numbers()
    print("The new numbers are : ", Square_Cube(numbers))
