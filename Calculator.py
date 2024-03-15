import tkinter as tk
from tkinter import messagebox

# Function to perform addition
def add():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform subtraction
def subtract():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform multiplication
def multiply():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform division
def divide():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Initialize Tkinter
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields
num1_label = tk.Label(root, text="Enter first number:")
num1_label.grid(row=0, column=0, padx=5, pady=5)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

num2_label = tk.Label(root, text="Enter second number:")
num2_label.grid(row=1, column=0, padx=5, pady=5)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add", command=add)
add_button.grid(row=2, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.grid(row=2, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=3, column=0, padx=5, pady=5)

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.grid(row=3, column=1, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()
