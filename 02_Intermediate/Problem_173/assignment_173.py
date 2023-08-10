'''
Write a Python program to multiply with every number 
with user entered number in a list.  When Number is Even
'''

def multiply_even_numbers(user_number, number_list):
    result = [num * user_number for num in number_list if num % 2 == 0]
    return result


if __name__=="__main__":
    user_number = int(input("Enter a number: "))
    number_list = [2, 4, 6, 8, 10, 12, 14]

    # Multiply even numbers by the user-entered number
    result_list = multiply_even_numbers(user_number, number_list)
    print("Result:", result_list)
