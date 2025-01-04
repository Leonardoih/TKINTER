import tkinter as tk
from tkinter import ttk
import time


class RelojDigital(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.overrideredirect(True)  # Elimina la barra de título
        self.geometry("300x100")
        self["bg"] = "black"

        # Frame para los botones y el título
        self.title_bar = tk.Frame(self, bg="black")
        self.title_bar.pack(fill='x', pady=2)

        # Botones estilo Mac
        # Botón cerrar (rojo)
        self.close_button = tk.Button(
            self.title_bar,
            text="",
            command=self.quit,
            bg="#FF5F57",
            fg="#FF5F57",
            relief="flat",
            width=1,
            height=1,
            font=("Arial", 1),
            borderwidth=0,
            cursor="hand2",
            padx=0,
            pady=0
        )
        self.close_button.pack(side="left", padx=4)

        # Botón minimizar (amarillo)
        self.minimize_button = tk.Button(
            self.title_bar,
            text="",
            command=self.minimizar,
            bg="#FFBD2E",
            fg="#FFBD2E",
            relief="flat",
            width=1,
            height=1,
            font=("Arial", 1),
            borderwidth=0,
            cursor="hand2",
            padx=0,
            pady=0
        )
        self.minimize_button.pack(side="left", padx=2)

        # Botón maximizar (verde)
        self.maximize_button = tk.Button(
            self.title_bar,
            text="",
            command=self.maximizar,
            bg="#28C940",
            fg="#28C940",
            relief="flat",
            width=1,
            height=1,
            font=("Arial", 1),
            borderwidth=0,
            cursor="hand2",
            padx=0,
            pady=0
        )
        self.maximize_button.pack(side="left", padx=2)

        # Título centrado
        self.title_label = tk.Label(
            self.title_bar,
            text="Reloj Digital",
            font=("Arial", 10),
            bg="black",
            fg="red"
        )
        self.title_label.pack(side="left", padx=80)

        # Permitir mover la ventana
        self.title_label.bind("<B1-Motion>", self.mover_ventana)
        self.title_label.bind("<Button-1>", self.guardar_posicion)

        # Configurar el estilo correctamente
        self.style = ttk.Style(self)
        self.style.configure(
            "Custom.TLabel",
            background="black",
            foreground="red"
        )

        # Usar el estilo personalizado en el label
        self.label = tk.Label(
            self, 
            text=self.tiempo_string(), 
            font=("Digital-7", 40),
            bg="black",
            fg="red"
        )
        self.label.pack(expand=True)
        self.label.after(1000, self.update)

        # Efectos hover para los botones
        def on_enter(e, color):
            e.widget['bg'] = self.adjust_color(color, 1.1)

        def on_leave(e, color):
            e.widget['bg'] = color

        # Configurar efectos hover
        self.close_button.bind('<Enter>', lambda e: on_enter(e, "#FF5F57"))
        self.close_button.bind('<Leave>', lambda e: on_leave(e, "#FF5F57"))
        self.minimize_button.bind('<Enter>', lambda e: on_enter(e, "#FFBD2E"))
        self.minimize_button.bind('<Leave>', lambda e: on_leave(e, "#FFBD2E"))
        self.maximize_button.bind('<Enter>', lambda e: on_enter(e, "#28C940"))
        self.maximize_button.bind('<Leave>', lambda e: on_leave(e, "#28C940"))

    def tiempo_string(self):
        return time.strftime("%H:%M:%S")

    def update(self):
        self.label.config(text=self.tiempo_string())
        self.label.after(1000, self.update)

    def guardar_posicion(self, event):
        self.x = event.x
        self.y = event.y

    def mover_ventana(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def minimizar(self):
        self.iconify()

    def maximizar(self):
        if self.state() == 'zoomed':
            self.state('normal')
        else:
            self.state('zoomed')

    def adjust_color(self, color, factor):
        # Convierte el color hex a RGB
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        # Ajusta el brillo
        r = min(int(r * factor), 255)
        g = min(int(g * factor), 255)
        b = min(int(b * factor), 255)
        
        # Convierte de vuelta a hex
        return f'#{r:02x}{g:02x}{b:02x}'

if __name__ == "__main__":
    reloj = RelojDigital()
    reloj.mainloop()
