import tkinter as tk
from tkinter import messagebox

class OddNumberApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Odd Number Application")

        self.number_list = []

        self.label = tk.Label(master, text="Enter 5 numbers:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_number)
        self.submit_button.pack()

        self.display_button = tk.Button(master, text="Display Odd Numbers", command=self.display_odd_numbers)
        self.display_button.pack()

    def submit_number(self):
        try:
            number = float(self.entry.get())
            self.number_list.append(number)
            self.entry.delete(0, tk.END)  
            if len(self.number_list) == 5:
                self.submit_button.config(state=tk.DISABLED)  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def display_odd_numbers(self):
        odd_numbers = [num for num in self.number_list if num % 2 != 0]
        message = f"Odd Numbers: {', '.join(map(str, odd_numbers))}"
        messagebox.showinfo("Odd Numbers", message)

def main():
    root = tk.Tk()
    app = OddNumberApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
