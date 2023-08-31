'''
Write A Python Program To Get 5 Items 
From A List That Are Divisible By 5 And 7, 
Not Included Last And First Item
'''

def get_divisible_items(lst):
    divisible_items = []
    for item in lst[1:-1]:
        if item % 5 == 0 and item % 7 == 0:
            divisible_items.append(item)

        if len(divisible_items) == 5:
            break
    return divisible_items

if __name__=="__main__":
    my_list = [10, 35, 14, 21, 70, 56, 105, 30, 49]

    result = get_divisible_items(my_list)
    print("Items divisible by 5 and 7 (excluding first and last):", result)
