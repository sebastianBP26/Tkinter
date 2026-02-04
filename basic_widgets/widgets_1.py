# Formulario básico con Frame widgets

import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    
    def __init__(self):
        ## Tkinter app
        super().__init__()
        self.title('Aprendiendo widgets - Code')
        self.geometry('450x650')

        # Frame Widget
        # El administrador de geometría es el que administra los contenidos del Frame
            # Padding
            # Borders
        frame_1 = ttk.Frame(self, padding = '10', borderwidth= 2, relief='sunken')

        # Label Widget
        self.my_instructions_label = ttk.Label(frame_1, text = 'Estoy en Frame 1')

        # Entry widget
        self.my_entry = ttk.Entry(frame_1, width=15)

        # Creamos un botón para llamar a la función
        self.my_button = ttk.Button(frame_1, text = 'Soy un botón en el frame 1')

        # Posicionamos los widgets en la ventana
        frame_1.pack(fill = tk.BOTH, expand=True)
        self.my_instructions_label.pack(pady = 10)
        self.my_entry.pack(pady = 5)
        self.my_button.pack(pady = 10)

    
if __name__ == '__main__':
    app = Application()
    app.mainloop()
