from tkinter import Tk  # Importa correctamente la clase Tk

root = Tk()  # Usa Tk() con la "T" mayúscula

# Cambiar el icono de la ventana
root.iconbitmap(r'TKINTER/icono.ico')

# Configuración de la ventana
root.title("Mi primer ventana")  # Poniendo nuestro primer título
root.geometry("500x300")  # Dándole las dimensiones a nuestra ventana

root.resizable(0,0) # hacemos que nuetra ventan no se modifique ni a lo ancho ni a lo largo

root.configure(bg="blue", cursor="sizing") # cambiamoe l fondo y el diseño del raton

root.mainloop()  # Inicia el bucle principal de la ventana

