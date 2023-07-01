'''
Write A Python Program To Get A Sentence From A User, 
User Should Able To Remove Any Character From A String
'''
def remove_character(sentence, char):
    new_sentence = sentence.replace(char, '')
    return new_sentence

if __name__=="__main__":
    sentence = input("Enter a sentence: ")
    char = input("Enter a character to remove: ")
    new_sentence = remove_character(sentence, char)
    print("Modified sentence:", new_sentence)

