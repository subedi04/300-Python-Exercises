'''
Write a Python Program to Create a dictionary 
which display those value which have vowel character.
'''
if __name__=="__main":
    d = {1:"Rd",14:"Blue",2:"Yellow",6:"Black",9:"JFR"}
    print(d)
    # a e o i u 
    for value in d.values():
        if 'a' in value or 'e' in value or 'o' in value or 'i' in value or 'u' in value:
            print(value)
