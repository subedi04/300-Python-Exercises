"""
Write a Python program that matches a word containing '6' digit.
"""
import re

def match_word_with_6_digits(word):
    pattern = r'\b\w*\d{6}\w*\b'
    result = re.search(pattern, word)
    if result:
        return result.group()
    else:
        return None


if __name__=="__main__":
    words = ['apple', '123456', 'abc123def', '12abcdefg', 'abcdefg123456']
    for word in words:
        matched_word = match_word_with_6_digits(word)
        print(f'Word: {word}, Matched word: {matched_word}')
