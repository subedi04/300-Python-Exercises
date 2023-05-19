'''
Write A Python Program To Get A Sentence From The User, T
o Reverse That Sentence
'''
# to get sentence/word to reverse
# display to user

def reverse_sent(st):
    reverse_st = ""
    for i in st:
        reverse_st = i + reverse_st
    return reverse_st  

if __name__=="__main__":
    st = input("Enter a sentece to reverse : ")  #jafri
    rev_st = reverse_sent(st)
    print(rev_st)

