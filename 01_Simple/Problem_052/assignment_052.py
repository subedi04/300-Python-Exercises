'''
Write A Python Program To Get A Sentence From The User, 
To Reverse That Sentence And Enclose In Double Quotations 
And Put A Full Stop At The End Of Sentence
'''

def reverse_sent(st):
    reverse_st = ""
    for i in st:
        reverse_st = i + reverse_st
    reverse_st = '"' + reverse_st + '."'
    return reverse_st  

if __name__=="__main__":
    st = input("Enter a sentece to reverse : ")  #jafri
    rev_st = reverse_sent(st)
    print(rev_st)
