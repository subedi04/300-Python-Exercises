'''
Write a Python Program to find minimum number from array.
'''
def find_minimum_number(num_list):
    if not num_list:
        return None

    min_number = num_list[0]
    for num in num_list:
        if num < min_number:
            min_number = num

    return min_number

if __name__=="__main__":
	numbers = [10, 5, 7, 3, 8, 2, 9, 4, 6, 1]

	# Find the minimum number
	min_num = find_minimum_number(numbers)

	if min_num is not None:
		  print("Minimum number: ", min_num)
	else:
		  print("The array is empty.")


