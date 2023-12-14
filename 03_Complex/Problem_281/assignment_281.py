import tkinter as tk
from tkinter import messagebox

class StudentSorterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Sorter")

        self.student_list = []

        # GUI Components
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()

        self.sort_button = tk.Button(master, text="Sort and Display", command=self.sort_and_display)
        self.sort_button.pack()

    def add_student(self):
        student_name = self.entry.get()
        if student_name:
            self.student_list.append(student_name)
            messagebox.showinfo("Success", "Student added successfully!")
            self.entry.delete(0, tk.END)  # Clear the entry field
        else:
            messagebox.showwarning("Error", "Please enter a student name.")

    def sort_and_display(self):
        if not self.student_list:
            messagebox.showwarning("Error", "Student list is empty.")
            return

        # Sort the student list
        sorted_students = sorted(self.student_list)

        # Filter names with exactly 5 characters
        filtered_students = [name for name in sorted_students if len(name) == 5]

        # Display the sorted and filtered names
        result_text = "\n".join(filtered_students)
        messagebox.showinfo("Sorted and Filtered Students", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSorterApp(root)
    root.mainloop()
