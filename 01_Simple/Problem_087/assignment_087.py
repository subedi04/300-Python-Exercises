'''
Write A Python Program To Get A Sentence From User, 
The System Should Display All Characters Except Last Ten Character
'''

def Remove_Ten_Element():
    sentence = input("Enter a sentence: ")
    length = len(sentence)


    if length >= 10:
        new_sentence = sentence[:-10]
    else:
        new_sentence = sentence

    print("Modified sentence:", new_sentence)

if __name__=="__main__":
    Remove_Ten_Element()