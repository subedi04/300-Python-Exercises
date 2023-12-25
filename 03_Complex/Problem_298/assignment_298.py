import tkinter as tk
from tkinter import messagebox

class ColorListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Color List Application")

        self.color_list = []

        self.label = tk.Label(master, text="Enter 5 color names:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_color)
        self.submit_button.pack()

        self.process_button = tk.Button(master, text="Process Colors", command=self.process_colors)
        self.process_button.pack()

    def submit_color(self):
        color = self.entry.get()
        if color:
            self.color_list.append(color)
            self.entry.delete(0, tk.END)  # Clear the entry field after submission
            if len(self.color_list) == 5:
                self.submit_button.config(state=tk.DISABLED)  # Disable the button after 5 colors are entered
        else:
            messagebox.showwarning("Warning", "Please enter a color name.")

    def process_colors(self):
        if len(self.color_list) >= 3:
            self.color_list.pop(0)  # Remove the first color
            self.color_list.pop(-1)  # Remove the last color

            message = f"All Colors: {', '.join(self.color_list)}\n"

            three_char_colors = [color for color in self.color_list if len(color) == 3]
            if three_char_colors:
                message += f"Colors with 3 characters: {', '.join(three_char_colors)}"
            else:
                message += "No colors with 3 characters."

            messagebox.showinfo("Color List", message)
        else:
            messagebox.showwarning("Warning", "Please enter at least 5 color names.")

def main():
    root = tk.Tk()
    app = ColorListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
