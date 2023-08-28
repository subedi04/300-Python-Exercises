'''
Write A Python Program To Convert Binary 
Into Decimal Number Using Recursion
'''

def binary_to_decimal(binary, index=0):
    if index == len(binary):
        return 0
    else:
        bit = int(binary[index])
        power = len(binary) - index - 1
        decimal = bit * (2 ** power)
        return decimal + binary_to_decimal(binary, index + 1)

def main():
    binary_input = input("Enter a binary number: ")
    
    # Remove leading zeros from the input
    binary_input = binary_input.lstrip("0")
    
    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal equivalent is: {decimal_output}")

if __name__ == "__main__":
    main()
