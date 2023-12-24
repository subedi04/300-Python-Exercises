import tkinter as tk
from tkinter import scrolledtext

class ScrollbarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Scrollbar Application")

        # Create a Text widget with a vertical scrollbar
        self.text_widget = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_widget.pack(pady=10)

        # Insert some text into the Text widget
        self.text_widget.insert(tk.END, "This is a sample text. " * 10)

        # Create a vertical scrollbar and associate it with the Text widget
        scrollbar = tk.Scrollbar(master, command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Text widget to use the scrollbar
        self.text_widget.config(yscrollcommand=scrollbar.set)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollbarApp(root)
    root.mainloop()
