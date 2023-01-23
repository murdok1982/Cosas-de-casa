import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=4)

button_list = [
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    ".", "0", "=", "/"
]

for i in range(16):
    button = tk.Button(button_frame, text=button_list[i], width=5, height=2, command=lambda x=button_list[i]: entry.insert(tk.END, x))
    button.grid(row=i//4, column=i%4)

clear_button = tk.Button(root, text="Clear", width=5, height=2, command=clear)
clear_button.grid(row=5, column=0, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", width=5, height=2, command=calculate)
calculate_button.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
