import tkinter as tk

def calculate():
    try:
        # Get numbers from the entry widgets
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Calculate the square of each number
        square1 = num1 ** 2
        square2 = num2 ** 2

        # Add the squares
        result = square1 + square2

        # Calculate the cube of the result
        result_cube = result ** 3

        # Display the result in the result_label
        result_label.config(text=f"Cube of the sum of squares: {result_cube}")

    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Number Operations")

# Create and place entry widgets for user input
label_num1 = tk.Label(root, text="Enter Number 1: ")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Enter Number 2: ")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Create and place a button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
root.mainloop()
