'''
Write A Python Program To Get 10 Float Data Type From User. 
System Should Convert Float Data Type Data To Integer
'''

def Float_to_Int():
    nums = [] 

    for i in range(10):
        n = float(input("Enter a float num : "))
        nums.append(n)
    
    for i in range(len(nums)) : 
        nums[i] = int(nums[i])

    print(nums)

if __name__=="__main__":
    Float_to_Int()