'''
Write a Python Program to Reverse array element using OOP.
'''

class ArrayReverser:
    def __init__(self, num_list):
        self.num_list = num_list

    def reverse_array(self):
        self.num_list.reverse()

    def display_array(self):
        print("Reversed Array: ", self.num_list)


if __name__=="__main__":
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	array_reverser = ArrayReverser(numbers)

	print("Initial Array: ")
	array_reverser.display_array()
	array_reverser.reverse_array()
	print("Reversed Array: ")
	array_reverser.display_array()

