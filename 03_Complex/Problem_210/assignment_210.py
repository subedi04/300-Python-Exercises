'''
Write A Python Program To Count Number Of 
Characters Other Than Vowel In Words.
'''

def count_non_vowel_characters(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char not in vowels and char.isalpha():
            count += 1

    return count

if __name__=="__main__":
    word = input("Enter a word: ")
    result = count_non_vowel_characters(word)
    print(f"Number of non-vowel characters in '{word}' is: {result}")
