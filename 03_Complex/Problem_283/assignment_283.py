import tkinter as tk

class UppercaseWordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Uppercase Words Collector")

        self.uppercase_words_list = []

        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Enter text:")
        self.label.pack(pady=10)

        # Text Entry
        self.text_entry = tk.Entry(self.root, width=30)
        self.text_entry.pack(pady=10)

        # Button
        self.collect_button = tk.Button(self.root, text="Collect Uppercase Words", command=self.collect_words)
        self.collect_button.pack(pady=10)

        # Display Uppercase Words
        self.display_label = tk.Label(self.root, text="Uppercase Words:")
        self.display_label.pack()

        # Listbox to display uppercase words
        self.listbox = tk.Listbox(self.root, height=5, selectmode=tk.MULTIPLE)
        self.listbox.pack()

    def collect_words(self):
        # Get text from the entry
        user_text = self.text_entry.get()

        # Extract uppercase words and store them in the list
        uppercase_words = [word for word in user_text.split() if word.isupper()]

        # Display uppercase words in the listbox
        self.listbox.delete(0, tk.END)
        for word in uppercase_words:
            self.listbox.insert(tk.END, word)

        # Add uppercase words to the overall list
        self.uppercase_words_list.extend(uppercase_words)

if __name__ == "__main__":
    root = tk.Tk()
    app = UppercaseWordsApp(root)
    root.mainloop()
