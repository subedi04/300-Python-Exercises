'''
Write a Python Program to Create a Dictionary 
to find addition of all the keys and Product 
of all the values from a dictionary.
'''
def addition_keys(d):
    keys = []
    for k in d.keys():
        keys.append(k)
    print(keys)

    addition = 0
    for i in keys:
        addition += i
    print(addition)

def dot_values(d):
    values = []
    for v in d.values():
        values.append(v)
    print(values)

    product = 1
    for i in values:
        product*= i
    print(product)

if __name__=="__main__":
    d = {1:100,14:14000,2:2000,6:6000,9:9000}
    print(d)

    addition_keys(d)
    dot_values(d)