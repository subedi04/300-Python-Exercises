'''
Write a Python Program to find average of 5 number using OOP.
'''

class AverageCalculator:
    def __init__(self):
        self.numbers = []

    def input_numbers(self):
        for i in range(5):
            number = float(input(f"Enter number {i + 1}: "))
            self.numbers.append(number)

    def calculate_average(self):
        total = sum(self.numbers)
        average = total / len(self.numbers)
        return average

def main():
    calculator = AverageCalculator()
    calculator.input_numbers()
    average = calculator.calculate_average()
    print(f"The average of the numbers is: {average:.2f}")

if __name__ == "__main__":
    main()
