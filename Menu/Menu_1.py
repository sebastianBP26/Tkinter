import tkinter as tk
from tkinter import ttk

import os
os.environ['XDG_CURRENT_DESKTOP'] = 'Unity'

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Uso de Menus - Code With Goz")
        self.geometry("1024x650")
        self.file_path = None

        ############################################################
        # Menu Widgets
        ############################################################
        # Los menus son implementados como widgets, cada menú
        # consiste de un número diferente de elementos de menú.
        # Los elementos tienen varios atributos

        # Para conocer la plataforma en la que se está ejecutando
        # el programa (x11, win32, aqua) 
        print(self.call('tk', 'windowingsystem'))

        # add_command(): agregar un elementto clickeable al menú el cual se linkea a una función

        # add_cascade(): agrega un mení drop-down linkeando al elemento de un menú a otro objeto menú

        # add_separator(): agrega un separador horizontal

        # tearoff=0: nunca olvidarlo, previene que el menú se despliegue como otra ventana.

        # Creamos menubar
        self.menubar = tk.Menu(self)
        # Agregamos el menubar a la ventana
        self.config(menu=self.menubar)

        # Creamos el submenu file_menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        # Agregamos un nombre al submenu
        self.menubar.add_cascade(label="Archivo", menu=self.file_menu)
        # Agregamos elementos al fle_menu
        self.file_menu.add_command(label="Nuevo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_command(label="Guardar como...", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit)

        # Creamos el submenu calculation_menu
        self.calculation_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Calcular", menu=self.calculation_menu)
        self.calculation_menu.add_command(label="Sumas", command=self.my_sum, accelerator='Ctrl+A')
        self.calculation_menu.add_command(label="Restas", command=self.my_function)
        self.calculation_menu.add_command(label="Multiplicaciones", command=self.my_function)
        self.calculation_menu.add_command(label="Divisiones", command=self.my_function)

        self.calculation_menu.entryconfigure('Divisiones', state=tk.DISABLED)
        #self.calculation_menu.entryconfigure('Divisiones', state=tk.NORMAL)

        # Creamos un submenu para el submenu
        self.graph_menu = tk.Menu(self.calculation_menu, tearoff=0)
        self.calculation_menu.add_cascade(label="Otros", menu=self.graph_menu)
        self.graph_menu.add_command(label="Grafica de barras", command=self.my_function)
        self.graph_menu.add_command(label="Grafica de circulo", command=self.my_function)

        self.bind_all("<Control-A>", self.my_sum)
        self.bind_all("<Control-a>", self.my_sum)

        ############################################################
        # Posicionamos los Widgets en ventana
        ############################################################


    def new_file(self):
        print('Presionaste nuevo archivo')

    def open_file(self):
        pass

    def save_file(self):
        pass

    def save_file_as(self):
        pass   

    def my_function(self):
        pass

    def my_sum(self, *event):
        print('Presionaste suma')    


if __name__ == "__main__":
    app = Application()
    app.mainloop()


