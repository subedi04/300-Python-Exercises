'''
Write a Python program to check alpha character, 
whether vowel or consonant. And also display “it is number”, 
if user give any number.
'''


def is_Alpha_Char_Number(char):
    if char.upper():
        char = char.lower()
        
    if((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u')):
        print("It is vowel")
    elif char.isdigit():
        print("The char is number : ", char)
    else:
        print("It is cons..")
    

if __name__=="__main__":
    char = input("Enter a char or number : ")
    is_Alpha_Char_Number(char)