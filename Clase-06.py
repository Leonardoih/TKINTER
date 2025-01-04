from tkinter import *
root = Tk()
root.config(bg="goldenrod3",bd=20)
root.title("Casa de Comidas")

# def orden():
#     # Lista=""
#     if queso.get() == 1 and lechuga.get() == 1:
#         imprimir.config(text="Tu pedido es: Hamburguesa con Queso y Lechuga")
#     elif queso.get() == 1 and lechuga.get() == 0:
#         imprimir.config(text="Tu pedido es: Hamburguesa con Queso")
#     elif queso.get() == 0 and lechuga.get() == 1:
#         imprimir.config(text="Tu pedido es: Hamburguesa con Lechuga")   
#     else :
#         imprimir.config(text="Tu pedido es: sin queso y sin lechuga")

def orden():
    lista=""
    if queso.get():
        lista += " con Queso"
    else:
        lista += " sin Queso"    
    if lechuga.get():
        lista += " y con Lechuga"
    else:
        lista += " y sin Lechuga"
    imprimir.config(text=f"Tu pedido es: Hamburguesa {lista}")

queso= IntVar()
lechuga= IntVar()

imagen = PhotoImage(file="Hamburguesa.png")

Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

Label(frame, text="Como quieres tu Hamburguesa?", font="Verdana 15 bold", bg="goldenrod3").pack(anchor="w")
Checkbutton(frame, text="Con Queso",variable=queso,onvalue=1,offvalue=0, font="Verdana 10", bg="goldenrod3", command=orden).pack(anchor="w")
Checkbutton(frame, text="Con Lechuga",variable=lechuga,onvalue=1,offvalue=0, font="Verdana 10", bg="goldenrod3", command=orden).pack(anchor="w")

imprimir = Label(frame,  font="Verdana 15 bold", bg="goldenrod3")
imprimir.pack(anchor="w")







root.mainloop()

