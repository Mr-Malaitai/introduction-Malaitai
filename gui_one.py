import tkinter as tk        # this is used to create a GUI
from tkinter import ttk     # ttk is used to adapt to the OS (operating system)

def convert_temp():
    # 1. Get temperature from Entry widget
    temperature = entry_widget.get()
    temperature = int(temperature)
    
    # 2. Find if user wants F to C or C to F
    if(temp.get()==1):
        result_temp = (temperature - 32) * 5/9
    
    elif(temp.get()==2):
        result_temp = (temperature * 9/5) + 32

    # 3. Calculate result (F to C = x minus 32 * 5/9)
    
    # 4. Display result
    result_label.configure(text="Result: {}".format(result_temp))

root = tk.Tk()              # this creates the window

temp = tk.IntVar()
temp.set(1)

# Title label for window
title_label = tk.Label(root, text="Temperature Convertor")
title_label.grid(row=0, column=0, columnspan=2)

# Entry widget for entering temperature values
entry_widget = tk.Entry(root)
entry_widget.grid(row=1, column=0, columnspan=2)

# F to C Radiobutton
f_to_c = tk.Radiobutton(root, text="F to C", variable=temp, value=1)
f_to_c.grid(row=2, column=0)

# C to F Radiobutton
c_to_f = tk.Radiobutton(root, text="C to F", variable=temp, value=2)
c_to_f.grid(row=2, column=1)

# Button for converting temperature
convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.grid(row=3, column=0, columnspan=2)

# Result label to display conversion
result_label = tk.Label(root, text="Result: -")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()             # this loops through the widgets