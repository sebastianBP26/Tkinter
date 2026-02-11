import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aprendiendo Widgets - Code With Goz")
        self.geometry("550x350")

        ############################################################
        # Widgets
        ############################################################

        frame_1 = ttk.Frame(self, padding="10")

        ############################################################
        # Entry Widget
        ############################################################
        # Campo de entrada para que los usuarios ingresen info
        # No tienen texto o imágenes asociadas
        # No tienen un command option para invocar un callback

        # Creamos un entry
        ############################################################
        self.name_var = tk.StringVar(self)
        self.name_entry = ttk.Entry(frame_1, width=26, textvariable=self.name_var)
 

        # Creamos un entry en el que observamos los cambios
        ############################################################
        self.name2_var = tk.StringVar(self)
        self.name2_entry = ttk.Entry(frame_1, width=26, textvariable=self.name2_var)
        # Podemos observar los cambios invocando callbacks 
        # read, write, delete. Así como removerlos con trace_remove
        self.name2_var.trace_add("write", self.it_has_been_written)


        # Creamos un entry de password
        ############################################################
        self.password_var = tk.StringVar(self)
        self.password_entry = ttk.Entry(frame_1, textvariable=self.password_var, show='*')

        # Creamos un entry deshabilitado
        ############################################################
        self.name3_var = tk.StringVar(self)
        self.name3_entry = ttk.Entry(frame_1, textvariable=self.name3_var)
        self.name3_entry.state(['disabled'])  
        self.name3_entry.state(['!disabled'])  


        ############################################################
        # Posicionamos los Widgets en ventana
        ############################################################
        frame_1.pack(fill=tk.BOTH, expand=True)
        
        self.name_entry.pack()
        self.name2_entry.pack()
        self.password_entry.pack()
        self.name3_entry.pack()



    def it_has_been_written(self, *args):
        print(f'Escribiste {self.name2_var.get()}')





if __name__ == "__main__":
    app = Application()
    app.mainloop()







