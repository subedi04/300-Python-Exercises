'''
Write A Python Program To Get String From 
User To Display Required Character 
That Present On Odd Index Number. 
Required Character Get From User
'''


if __name__=="__main__":
    input_string = input("Enter a string: ")

    # Get the character to search for
    search_char = input("Enter the character to search for: ")

    # Initialize a variable to store the result
    result = ""

    # Iterate through the string and add characters at odd indices
    for index in range(len(input_string)):
        if index % 2 != 0 and input_string[index] == search_char:
            result += input_string[index]

    # Check if any matching characters were found
    if result:
        print(f"Characters '{search_char}' at odd indices: {result}")
    else:
        print(f"No '{search_char}' characters found at odd indices in the string.")

