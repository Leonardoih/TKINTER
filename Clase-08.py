from tkinter import *
from tkinter import messagebox


root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)

def cerrar():
    respuesta = messagebox.askquestion("cerrar" , message="¿Estas seguro de cerrar la aplicacion?", icon="warning")
    if respuesta == "yes":
        root.quit()
    else:
        pass
    
def licencia():
    messagebox.showinfo("Licencia", "Este programa es de uso libre \n Licencia GPL")
    
def error():
    messagebox.showerror("ERROR CRITICO", message="SE ENCONTRO UN ERROR FATAL EN EL SISTEMA")
    
def ateencion():
    messagebox.showwarning("Atencion", message="Este programa esta en fase de desarrollo")
    

archivoMenu = Menu(menuBar, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir",  command=ateencion)
archivoMenu.add_command(label="Guardar", command=error)
archivoMenu.add_command(label="Cerrar", command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=root.quit)

editarMenu = Menu(menuBar, tearoff=0)

editarMenu.add_command(label="Cortar")
editarMenu.add_command(label="Copiar")
editarMenu.add_command(label="Pegar")


ayudaMenu = Menu(menuBar, tearoff=0)

ayudaMenu.add_command(label="Ayuda" , command=licencia)
# ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
menuBar.add_cascade(label="Editar", menu=editarMenu)
menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)



root.mainloop()