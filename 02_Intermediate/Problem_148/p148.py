'''
Write a Python Program Create dictionary from 
existed dictionary which display length of words 
as value
'''
if __name__=="__main__":
    d = {"name":"Faisal Zamir","age":13,"course":"Python","City":"Dera Ismail Khan"}
    print(d)
    new_dic = {k:len(k)  for k,v in d.items()}
    print(new_dic)