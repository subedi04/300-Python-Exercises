'''
Write A Python Program To Get 
A Paragraph From User, To Find
(total Char, Total Words, Total 
Vowel Char And Spaces)
'''

def count_vowels(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    paragraph = input("Enter a paragraph: ")

    total_chars = len(paragraph)
    total_words = len(paragraph.split())
    total_vowels = count_vowels(paragraph)
    total_spaces = paragraph.count(" ")

    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Total vowel characters: {total_vowels}")
    print(f"Total spaces: {total_spaces}")

if __name__ == "__main__":
    main()
