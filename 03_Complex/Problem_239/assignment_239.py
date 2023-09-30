'''
Write a Python Program To Get a Sentence From
User And Also Get a Char Or Set Of Char To Check 
At Start of Sentence.
'''

if __name__=="__main__":

    sentence = input("Enter a sentence: ")

    start_chars = input("Enter the character or set of characters to check at the start: ")

    # Check if the sentence starts with the specified characters
    if sentence.startswith(start_chars):
        print(f"The sentence '{sentence}' starts with '{start_chars}'.")
    else:
        print(f"The sentence '{sentence}' does not start with '{start_chars}'.")
