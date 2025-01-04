from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x300")

w = Spinbox(root, values=("Python", "Java", "C++", "C#"))
w.pack()

e = Spinbox(root, values=("carne", "pollo", "pescado", "vegetariano","vegano"))
e.pack()














root.mainloop()