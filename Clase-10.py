from tkinter import *

root= Tk()
root.geometry("400x300")

productos = Label(root, text="Productos")
productos.pack()

def agregarProducto():
    producto = entrada.get()
    if producto:  # Verifica si se ha ingresado algo
        ListaProductos.insert(END, producto)
        entrada.delete(0, END)

def limpiarLista():
    ListaProductos.delete(0, END)

ListaProductos = Listbox(root, width=50)
ListaProductos.insert(1, "Leche")
ListaProductos.insert(2, "Pan")
ListaProductos.insert(3, "Huevos")
ListaProductos.insert(4, "Carne")
ListaProductos.insert(5, "Pollo")
ListaProductos.insert(6, "Pescado")
ListaProductos.insert(7, "Frutas")
ListaProductos.insert(8, "Verduras")
ListaProductos.insert(9, "Legumbres")
ListaProductos.insert(10, "Granos")
ListaProductos.insert(11, "Canela")
ListaProductos.pack()

#Eliminar productos


ListaProductos.delete(2)

entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text="Agregar Producto", bd=10 , command=agregarProducto)
boton.pack()

#Crear boton para limpiar lista
boton_limpiar = Button(root, text="Limpiar Lista", bd=10, command=limpiarLista)
boton_limpiar.pack()

root.mainloop()