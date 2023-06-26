'''
Write A Python Program To Find Occurrence 
Of A Specific Word Or Characters In A Sentence, 
Then Replace With Another Word Or Characters
'''
def replace_word(sentence, target_word, replacement_word):
    replaced_sentence = sentence.replace(target_word, replacement_word)
    return replaced_sentence


def main():
    sentence = input("Enter a sentence: ")
    target_word = input("Enter the word or characters to replace: ")
    replacement_word = input("Enter the replacement word or characters: ")

    replaced_sentence = replace_word(sentence, target_word, replacement_word)
    print("Replaced sentence:", replaced_sentence)

if __name__=="__main__":
    main()
