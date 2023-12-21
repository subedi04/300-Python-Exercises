import tkinter as tk

class NumberAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Analyzer")

        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label1 = tk.Label(self.root, text="Enter the first number:")
        self.label1.pack(pady=10)

        self.label2 = tk.Label(self.root, text="Enter the second number:")
        self.label2.pack(pady=10)

        # Text Entry for numbers
        self.entry1 = tk.Entry(self.root, width=30)
        self.entry1.pack(pady=5)

        self.entry2 = tk.Entry(self.root, width=30)
        self.entry2.pack(pady=5)

        # Button
        self.analyze_button = tk.Button(self.root, text="Analyze Numbers", command=self.analyze_numbers)
        self.analyze_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def analyze_numbers(self):
        # Get numbers from the entry fields
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")
            return

        # Find maximum, minimum, and check if numbers are equal
        max_num = max(num1, num2)
        min_num = min(num1, num2)

        result_message = f"Maximum Number: {max_num}\nMinimum Number: {min_num}\n"

        if num1 == num2:
            result_message += "Numbers are equal to each other."
        else:
            result_message += "Numbers are not equal."

        # Display whether numbers are positive or negative
        if num1 > 0:
            result_message += "\nFirst number is positive."
        elif num1 < 0:
            result_message += "\nFirst number is negative."

        if num2 > 0:
            result_message += "\nSecond number is positive."
        elif num2 < 0:
            result_message += "\nSecond number is negative."

        # Update result label
        self.result_label.config(text=result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberAnalyzerApp(root)
    root.mainloop()
