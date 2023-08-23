'''
Write a Python Program to remove any specific element from array using OOP. 
'''

class ArrayManipulator:
    def __init__(self, num_list):
        self.num_list = num_list

    def remove_element(self, element):
        if element in self.num_list:
            self.num_list.remove(element)
            print(f"Element {element} removed successfully.")
        else:
            print(f"Element {element} not found in the array.")

    def display_array(self):
        print("Array:", self.num_list)


if __name__=="__main__":
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	array_manipulator = ArrayManipulator(numbers)

	print("Initial Array: ")
	array_manipulator.display_array()

	# Remove a specific element
	element_to_remove = 5
	array_manipulator.remove_element(element_to_remove)

	# Display the updated array
	print("Updated Array: ")
	array_manipulator.display_array()

