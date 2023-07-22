'''
Write a Python program to get the total length 
of all keys of a dictionary with string keys. 
'''

if __name__=="__main__":
    d = {"color1":"Red","color2":"Blue","color3":"Yellow","color4":"Black","color5":"Green"}
    print(d)
    a = 0
    for i in d.keys():
        a  += len(i)

    print(a)