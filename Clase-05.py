from tkinter import *
#esta aplicacion se encarga de crear una ventana con dos entradas de texto y un boton para saludar

#crear la ventana
root =Tk()
root.title("Radiosbuttons")
root.geometry("400x300")
root.config(bg="goldenrod3")
root.resizable(0,0)

#funcion para realizar la operacion
def operacion():
    numero = int(entrada1.get())
    if opcion.get() == 1:
        total = numero*5
    elif opcion.get() == 2:
        total = numero*10
    elif opcion.get() == 3:
        total = numero*20
    elif opcion.get() == 4:
        total = numero*30
    elif opcion.get() == 5:
        total = numero*40
    else:
        total = numero * numero
    print(f"El total de la operacion es : {str(total)}")


opcion= IntVar()
num= IntVar()




#crear etiquetas y entradas
etiqueta1 = Label(root, text = " Escribe tu numero" , bg="goldenrod3", bd=5)
etiqueta1.place(x=20, y = 20)

entrada1 = Entry(root, bd=7, font="Helvetica 12")
entrada1.place(x=150, y = 20)

etiqueta2 = Label(root, text = " Elija la cantidad : ", bg="goldenrod3", bd=5)
etiqueta2.place(x=20, y=50)

x5 = Radiobutton(root, text = "x5", value=1, bg="goldenrod3", bd=5, variable=opcion)
x5.place(x=20, y=80)

x10 = Radiobutton(root, text = "x10", value=2, bg="goldenrod3", bd=5, variable=opcion)
x10.place(x=70, y=80)

x20 = Radiobutton(root, text = "x20", value=3, bg="goldenrod3", bd=5, variable=opcion)
x20.place(x=120, y=80)

x30 = Radiobutton(root, text = "x30", value=4, bg="goldenrod3", bd=5, variable=opcion)
x30.place(x=20, y=110)

x40 = Radiobutton(root, text = "x40", value=5, bg="goldenrod3", bd=5, variable=opcion)
x40.place(x=70, y=110)

boton1 = Button(root, text="Realizar Operacion", bg="goldenrod3", bd=5, command=operacion)
boton1.place(x=20, y=140)








root.mainloop()