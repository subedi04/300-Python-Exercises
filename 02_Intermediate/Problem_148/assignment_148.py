'''
Write a Python Program Create dictionary which display 
length of words as key. It should display length of value.
'''

def main():
    input_string = input("Enter a sentence: ")

    # Split the input sentence into words
    words = input_string.split()

    # Create an empty dictionary to store the word lengths
    word_lengths_dict = {}

    # Populate the dictionary with word lengths
    for word in words:
        word_length = len(word)
        if word_length not in word_lengths_dict:
            word_lengths_dict[word_length] = []
        word_lengths_dict[word_length].append(word_length)

    # Display the dictionary
    print("Word Lengths and their corresponding word lengths:")
    for length, lengths_list in word_lengths_dict.items():
        print(f"Length {length}: {lengths_list}")

if __name__ == "__main__":
    main()
