import tkinter as tk
from time import strftime

# Function to update time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create tkinter window
root = tk.Tk()
root.title("Clock")

# Create label for displaying time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

time()  

root.mainloop()
