'''
Write a Python Program to Display positive and negative in a list. 
When there is Positive and Negative number. Using list comprehension.
'''

if __name__=="__main__":
    lst = [1,2,3,-4,5,-3,9,-8]
    print(lst)
    new_list = [ "Positive" if i > 0 else "Negative" for i in lst]
    print(new_list)