'''
Write A Python Program To Get 10 Number From The User, 
Store Into List, Find Their Products And Sum. 
Then Add Both Result To Display To User
'''

def calculate_product(numbers):
    """
    Calculates the product of a list of numbers.
    
    Parameters:
        numbers (list): List of numbers.
    
    Returns:
        int or float: The product of the numbers.
    """
    product = 1
    for num in numbers:
        product *= num
    return product


def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.
    
    Parameters:
        numbers (list): List of numbers.
    
    Returns:
        int or float: The sum of the numbers.
    """
    total_sum = sum(numbers)
    return total_sum

def get_Data():
    # Get 10 numbers from the user
    numbers = []
    for i in range(10):
        number = float(input("Enter number {}: ".format(i + 1)))
        numbers.append(number)
    return numbers



if __name__=="__main__":
    # Get 10 numbers from the user
    numbers = get_Data()

    # Calculate the product of the numbers
    product = calculate_product(numbers)

    # Calculate the sum of the numbers
    total_sum = calculate_sum(numbers)

    # Add the product and sum
    result = product + total_sum

    # Display the result to the user
    print("Product:", product)
    print("Sum:", total_sum)
    print("Result (Product + Sum):", result)
