from tkinter import *
import time

root = Tk()
root.title = ("Python")
root.geometry("500x400")

boton1 = Button(root, text="Minimizar", command=root.iconify, bg="green")
boton1.pack(side=LEFT)

def imprimir():
    label1 = Label(root, text="Imprimiendo...")
    label1.pack()
    print("Botón 2 pulsado")

boton2 = Button(root, text="Imprimir", command=imprimir, bg="blue")
boton2.pack(side=RIGHT)


root.mainloop()