import tkinter as tk

class StringCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("String Counter")

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Enter a string:")
        self.label.pack(pady=10)

        # Text Entry
        self.text_entry = tk.Entry(self.root, width=30)
        self.text_entry.pack(pady=10)

        # Button
        self.count_button = tk.Button(self.root, text="Count", command=self.count_string)
        self.count_button.pack(pady=10)

        # Result Labels
        self.words_label = tk.Label(self.root, text="Total Words: ")
        self.words_label.pack()

        self.spaces_label = tk.Label(self.root, text="Total Spaces: ")
        self.spaces_label.pack()

        self.characters_label = tk.Label(self.root, text="Total Characters (without spaces): ")
        self.characters_label.pack()

    def count_string(self):
        # Get the input string from the entry
        user_string = self.text_entry.get()

        # Count words, spaces, and characters
        total_words = len(user_string.split())
        total_spaces = user_string.count(' ')
        total_characters_without_spaces = len(user_string) - total_spaces

        # Update result labels
        self.words_label.config(text=f"Total Words: {total_words}")
        self.spaces_label.config(text=f"Total Spaces: {total_spaces}")
        self.characters_label.config(text=f"Total Characters (without spaces): {total_characters_without_spaces}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringCounterApp(root)
    root.mainloop()
