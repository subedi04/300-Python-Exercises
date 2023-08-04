'''
Write a Python Program to display element of list 
with their occurrence using another method.
'''

def count_elements(lst):
    count = {}
    for element in lst:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    
    for element, occurrence in count.items():
        print(f"{element}: {occurrence}")
        
if __name__=="__main__":
    my_list = [1, 2, 3, 2, 4, 1, 5, 1]
    count_elements(my_list)
