import tkinter as tk
from tkinter import ttk

root = tk.Tk()

option_chosen = tk.IntVar()

message = ttk.Label(root, text = "Hello, World!")
message.grid(row = 0, column = 0)

submit_button = ttk.Button(root, text = "Submit")
submit_button.grid(row = 1, column = 0)

option_one = ttk.Radiobutton(root, text = "Option One", variable = option_chosen, value = 1)
option_one.grid(row = 2, column = 0)

option_two = ttk.Radiobutton(root, text = "Option Two", variable = option_chosen, value = 2)
option_two.grid(row = 3, column = 0)

root.mainloop()