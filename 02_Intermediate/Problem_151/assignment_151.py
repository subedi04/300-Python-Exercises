'''
Write a Python Program to Create a list from 
existed list that contain lowercase words
'''

def create_list(lst):
    lowercase_words = []
    for word in lst:
        if word.islower():
            lowercase_words.append(word)
    return lowercase_words

if __name__=="__main__":
    my_list = ["Hello", "world", "Python", "programming", "is", "fun"]
    lowercase_list = create_list(my_list)
    print(lowercase_list)
