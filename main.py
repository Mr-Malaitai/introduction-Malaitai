import tkinter as tk
from tkinter import ttk

root = tk.Tk()

message = ttk.Label(root, text="Hello, world!")
message.grid(row = 0, column = 0)

submit_button = ttk.Button(root, text = "Submit")
submit_button.grid(row = 1, column = 0)

root.mainloop()