import tkinter as tk
from tkinter import messagebox

class ColorListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Color List Application")

        self.color_list = []

        self.label = tk.Label(master, text="Enter 5 color names: ")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_color)
        self.submit_button.pack()

        self.display_button = tk.Button(master, text="Display List (Reverse Order)", command=self.display_list)
        self.display_button.pack()

    def submit_color(self):
        color = self.entry.get()
        if color:
            self.color_list.append(color)
            self.entry.delete(0, tk.END) 
            if len(self.color_list) == 5:
                self.submit_button.config(state=tk.DISABLED)  # Disable the button after 5 colors are entered
        else:
            messagebox.showwarning("Warning", "Please enter a color name.")

    def display_list(self):
        reversed_list = list(reversed(self.color_list))
        message = "Color List (Reverse Order):\n" + "\n".join(reversed_list)
        messagebox.showinfo("Color List", message)

def main():
    root = tk.Tk()
    app = ColorListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
