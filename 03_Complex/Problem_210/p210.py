'''
Write A Python Program To Count Number Of Vowel In Words
'''

if __name__=="__main__":
    user_s = input("Enter a sentence : ")
    vowel = 0
    for i in user_s:
        if i == "i" or i == "I" or i == "e" or i == "E" or i == "u" or i == "U" or i == "o" or i == "O" or i == "a" or i == "A":
            vowel += 1
    print("Total number of vowel char = "+str(vowel))