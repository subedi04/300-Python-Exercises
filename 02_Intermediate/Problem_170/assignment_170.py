'''
Write a Python Program to display positive, negative and Zero in a list. 
When there is positive, negative or Zero number. Using list comprehension.
'''

def classify_numbers(numbers):
    positive = [num for num in numbers if num > 0]
    negative = [num for num in numbers if num < 0]
    zero = [num for num in numbers if num == 0]
    
    return positive, negative, zero

if __name__=="__main__":
    numbers = [3, -2, 0, 5, -7, 0, 9, -1, 0]

    positive_nums, negative_nums, zero_nums = classify_numbers(numbers)

    print("Positive numbers:", positive_nums)
    print("Negative numbers:", negative_nums)
    print("Zero numbers:", zero_nums)
