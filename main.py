# print("Hello, World!")

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

submit_button = ttk.Button(root, text = "Submit")
submit_button.grid(row = 0, column = 0)

root.mainloop()