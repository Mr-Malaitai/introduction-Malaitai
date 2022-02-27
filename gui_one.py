import tkinter as tk        # this is used to create a GUI
from tkinter import ttk     # ttk is used to adapt to the OS (operating system)

root = tk.Tk()              # this creates the window

# Title label for window
title_label = tk.Label(root, text="Temperature Convertor")
title_label.grid(row=0, column=0, columnspan=2)

# Entry widget for entering temperature values
entry_widget = tk.Entry(root)
entry_widget.grid(row=1, column=0, columnspan=2)

# F to C Radiobutton
f_to_c = tk.Radiobutton(root, text="F to C")
f_to_c.grid(row=2, column=0)

# C to F Radiobutton
c_to_f = tk.Radiobutton(root, text="C to F")
c_to_f.grid(row=2, column=1)

# Button for converting temperature
convert_button = tk.Button(root, text="Convert")
convert_button.grid(row=3, column=0, columnspan=2)

# Result label to display conversion
result_label = tk.Label(root, text="Result: -")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()             # this loops through the widgets