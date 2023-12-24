import tkinter as tk
from tkinter import messagebox

class ListboxApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Listbox Application")

        # Create a Listbox
        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=10)

        # Add items to the Listbox
        items = ["Method 1", "Method 2", "Method 3", "Method 4"]
        for item in items:
            self.listbox.insert(tk.END, item)

        # Create a button to perform selected methods
        self.perform_button = tk.Button(master, text="Perform Selected Methods", command=self.perform_methods)
        self.perform_button.pack(pady=10)

    def perform_methods(self):
        selected_items = self.listbox.curselection()

        if not selected_items:
            messagebox.showinfo("No Selection", "Please select at least one method.")
            return

        selected_methods = [self.listbox.get(index) for index in selected_items]
        message = f"Selected methods: {', '.join(selected_methods)}"
        messagebox.showinfo("Selected Methods", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListboxApp(root)
    root.mainloop()
