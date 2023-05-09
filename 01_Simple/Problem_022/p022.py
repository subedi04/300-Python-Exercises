'''
Write A Python Program To Check Alpha Character, 
Whether Vowel Or Consonant.
'''
# to get char from user 
# check , vowel or not

def is_Alplha_Char(char):
    if char.upper():
        char = char.lower()
    
    if((char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u')):
        print("It is vowel")
    else:
        print("It is cons..")
    

if __name__=="__main__":
    char = input("Enter a char : ")
    is_Alplha_Char(char)

    
    
    #elif(char == 'e'):
#    print("It is vowel")
#elif(char == 'i'):
#    print("It is vowel")
#elif(char == 'o'):
#    print("It is vowel")
#elif(char == 'u'):
#    print("It is vowel")