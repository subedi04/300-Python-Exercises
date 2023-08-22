'''
Write a Python Program to count any array element 
from existed array using OOP
'''
class ArrayCounter:
    def __init__(self, array):
        self.array = array

    def count_element(self, element):
        count = 0
        for item in self.array:
            if item == element:
                count += 1
        return count

if __name__=="__main__":
	my_array = [1, 2, 3, 2, 4, 2, 5]
	counter = ArrayCounter(my_array)

	# Element to count
	element_to_count = 2

	# Count the element in the array
	element_count = counter.count_element(element_to_count)

	print(f"The element {element_to_count} appears {element_count} times in the array.")

