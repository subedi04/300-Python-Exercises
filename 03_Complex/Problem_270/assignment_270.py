def find_uppercase_sequence(string):
    uppercase_sequences = []
    i = 0
    while i < len(string):
        sequence = ''
        if string[i:i+4].isupper() and len(string[i:i+4]) == 4:
            sequence = string[i:i+4]
            uppercase_sequences.append(sequence)
            i += 4  # Skip 4 characters
        else:
            i += 1  # Move to the next character
    return uppercase_sequences

if __name__=="__main__":
    user_string = input("Enter a string: ")

    sequences = find_uppercase_sequence(user_string)

    if sequences:
        print(f"Sequences of 4 uppercase letters found: {sequences}")
    else:
        print("No sequences of 4 uppercase letters found in the string.")
