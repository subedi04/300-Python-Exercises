import tkinter as tk

class NumberCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Checker")

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Enter a number:")
        self.label.pack(pady=10)

        # Text Entry
        self.number_entry = tk.Entry(self.root, width=30)
        self.number_entry.pack(pady=10)

        # Button
        self.check_button = tk.Button(self.root, text="Check Number", command=self.check_number)
        self.check_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def check_number(self):
        # Get the input number from the entry
        try:
            user_number = float(self.number_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return

        # Check whether the number is negative, positive, or zero
        if user_number < 0:
            result_message = f"The number {user_number} is negative."
        elif user_number > 0:
            result_message = f"The number {user_number} is positive."
        else:
            result_message = "The number is zero."

        # Update result label
        self.result_label.config(text=result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberCheckerApp(root)
    root.mainloop()
