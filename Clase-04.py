from tkinter import *

#esta aplicacion se encarga de crear una ventana con dos entradas de texto y un boton para saludar

#Crear la ventana
root = Tk()
root.title("Entrada")
root.geometry("400x300")
root.resizable(0,0)


nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

nombre.set("")
apellido.set("")

def saludar():
    saludo.set(f"Hola {nombre.get()} {apellido.get()}")

etiqueta1 = Label(root, text="Escribe aqui tu nombre", bd=4, bg="green", font="Verdana  10")
etiqueta1.place(x=10, y=10)

entrada1= Entry(root, textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)


etiqueta2 = Label(root, text="Escribe aqui tu apellido", bd=4, bg="green", font="Verdana  10")
etiqueta2.place(x=10, y=40)

entrada2= Entry(root, textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar Ahora", command=saludar,  bd=5, bg="green")
boton.place(x=10, y=100)

entrada3 = Entry(root,  bd=20, font="verdana 10", textvariable=saludo, state="disabled")
entrada3.place(x=70, y=221)















root.mainloop()