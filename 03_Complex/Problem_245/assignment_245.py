'''
Write a Python program where a string will END with a number. 
'''

def end_with_number(string):
    if string[-1].isdigit():
        return True
    return False

if __name__=="__main__":
    print(end_with_number('this is a string'))
    print(end_with_number('this is a string 2'))
