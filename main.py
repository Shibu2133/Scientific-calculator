import tkinter as tk
from math import *

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to append characters to the expression

def append_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display the expression and result
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=6)

# Define button labels
button_labels = [
    '7', '8', '9', '/', 'sin', 'cos',
    '4', '5', '6', '*', 'tan', 'sqrt',
    '1', '2', '3', '-', 'log', 'exp',
    '0', '.', '(', ')', '^', 'pi',
    'C', '=', '+', 'e', 'x²', '1/x'
]

# Button creation loop
row = 1
col = 0
for label in button_labels:
    if label == '=':
        button = tk.Button(root, text=label, padx=20, pady=20, bg='lightblue',
                           command=evaluate_expression)
    elif label == 'C':
        button = tk.Button(root, text=label, padx=20, pady=20, bg='lightcoral',
                           command=clear_entry)
    else:
        button = tk.Button(root, text=label, padx=20, pady=20,
                           command=lambda label=label: append_to_expression(label))

    button.grid(row=row, column=col)
    col += 1
    if col > 5:
        col = 0
        row += 1

# Start the Tkinter event loop
root.mainloop()
