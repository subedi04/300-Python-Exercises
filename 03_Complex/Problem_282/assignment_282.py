import tkinter as tk
from tkinter import messagebox

class BookInfoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Information")

        self.author_book_data = []
        self.num_authors = 5

        # GUI Components
        self.label_author = tk.Label(master, text="Enter Author Name: ")
        self.label_author.pack()

        self.entry_author = tk.Entry(master)
        self.entry_author.pack()

        self.label_book = tk.Label(master, text="Enter Book Name: ")
        self.label_book.pack()

        self.entry_book = tk.Entry(master)
        self.entry_book.pack()

        self.add_button = tk.Button(master, text="Add Author and Book", command=self.add_author_and_book)
        self.add_button.pack()

        self.display_button = tk.Button(master, text="Display Last Author and Book", command=self.display_last_author)
        self.display_button.pack()

    def add_author_and_book(self):
        author_name = self.entry_author.get()
        book_name = self.entry_book.get()

        if author_name and book_name:
            self.author_book_data.append((author_name, book_name))
            messagebox.showinfo("Success", "Author and book added successfully!")
            self.entry_author.delete(0, tk.END)
            self.entry_book.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter both author name and book name.")

    def display_last_author(self):
        if not self.author_book_data:
            messagebox.showwarning("Error", "Author and book data is empty.")
            return

        last_author, last_book = self.author_book_data[-1]

        result_text = f"Last Author: {last_author}\nLast Book: {last_book}"
        messagebox.showinfo("Last Author and Book", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookInfoApp(root)
    root.mainloop()
