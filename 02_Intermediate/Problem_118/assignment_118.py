'''
Write a Python program to print a 
list from a nested list which have 
lowest number.
'''

def find_lowest_sublists(nested_list):
    lowest_number = float('inf')  # Initialize with positive infinity
    lowest_sublists = []

    # Find the lowest number in the nested list
    for sublist in nested_list:
        for number in sublist:
            if number < lowest_number:
                lowest_number = number

    # Find the sublists that contain the lowest number
    for sublist in nested_list:
        if lowest_number in sublist:
            lowest_sublists.append(sublist)

    return lowest_sublists


if __name__=="__main__":
    nested_list = [[3, 5, 2], [9, 8, 2], [4, 7, 6], [1, 9, 2], [4, 6, 2]]
    lowest_sublists = find_lowest_sublists(nested_list)

    print("Sublist(s) with the lowest number: ")
    for sublist in lowest_sublists:
        print(sublist)
