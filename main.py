import tkinter as tk
from tkinter import ttk

def display_option():

    display_message = ""
    
    if option_chosen == 1:
        display_message = "You have selected Option 1"
    elif option_chosen == 2:
        display_message = "You have selected Option 2"
    
    message.configure(text = display_message)

root = tk.Tk()

option_chosen = tk.IntVar(root)

message = ttk.Label(root, text = "Hello, World!")
message.grid(row = 0, column = 0)

option_one = ttk.Radiobutton(root, text = "Option One", variable = option_chosen, value = 1)
option_one.grid(row = 1, column = 0)

option_two = ttk.Radiobutton(root, text = "Option Two", variable = option_chosen, value = 2)
option_two.grid(row = 2, column = 0)

submit_button = ttk.Button(root, text = "Submit", command = display_option)
submit_button.grid(row = 3, column = 0)

root.mainloop()