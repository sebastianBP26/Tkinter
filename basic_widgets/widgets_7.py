# Combo Box Widget

import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    
    def __init__(self):
        ## Tkinter app
        super().__init__()
        self.title('Aprendiendo widgets - Code')
        self.geometry('1026x350')

        # Frame Widget
        frame_1 = ttk.Frame(self, padding = '10', borderwidth= 2, relief='sunken')

        # Combo Box
        self.country_var = tk.StringVar(self)
        self.country = ttk.Combobox(frame_1, # En dónde lo colocamos
                                    values=['Colombia', 'México', 'Perú', 'Argentina', 'Chile', 'Ecuador'], # Opciones en una lista
                                    textvariable=self.country_var, # Variable asociada
                                    state='readonly'
                                    )
        
        self.country.current(0) # Selecciona el primer elemento por defecto
        self.button = ttk.Button(frame_1, 
                                 text='Enviar', 
                                 command=self.show_option)


        frame_1.pack(fill='both', expand=True)
        self.country.pack(anchor='w', pady=6)
        self.button.pack(anchor='w', pady=6)

    def show_option(self):
        print(f'Seleccionaste: {self.country_var.get()}')
        
        
    
if __name__ == '__main__':
    app = Application()
    app.mainloop()