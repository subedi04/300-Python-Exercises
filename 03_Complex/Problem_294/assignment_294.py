import tkinter as tk
from tkinter import messagebox

class NumberListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Number List Application")

        self.number_list = []

        self.label = tk.Label(master, text="Enter 5 numbers:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_number)
        self.submit_button.pack()

        self.display_button = tk.Button(master, text="Display List", command=self.display_list)
        self.display_button.pack()

    def submit_number(self):
        try:
            number = float(self.entry.get())
            self.number_list.append(number)
            self.entry.delete(0, tk.END)  # Clear the entry field after submission
            if len(self.number_list) == 5:
                self.submit_button.config(state=tk.DISABLED)  # Disable the button after 5 numbers are entered
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def display_list(self):
        sorted_list = sorted(self.number_list)
        messagebox.showinfo("Number List", f"Sorted List: {sorted_list}")

def main():
    root = tk.Tk()
    app = NumberListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
