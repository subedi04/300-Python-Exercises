'''
Write A Python Program To Get A 
Sentence From User, To Count 
Specific Word In A Sentence
'''

def count_word(sentence, word):
    """
    Counts the number of occurrences of a specific word in a sentence.
    
    Parameters:
        sentence (str): The sentence to search for the word.
        word (str): The word to count in the sentence.
    
    Returns:
        int: The number of occurrences of the word in the sentence.
    """
    words = sentence.split()
    count = 0
    for w in words:
        if w.lower() == word.lower():
            count += 1
    return count


if __name__=="__main__":
    # Get sentence from user
    sentence = input("Enter a sentence: ")

    # Get word to count from user
    word = input("Enter a word to count: ")

    # Count the word in the sentence
    word_count = count_word(sentence, word)
    print("Occurrences of '{}' in the sentence: {}".format(word, word_count))
