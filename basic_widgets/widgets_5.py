# Formulario básico con Frame widgets

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

        # Checkbutton Widget
        self.status_var = tk.StringVar(self, value='ON')
        self.checkbutton_1 = ttk.Checkbutton(frame_1, 
                                             text = 'Encender', 
                                             command = self.status_changed,
                                             variable = self.status_var,
                                             onvalue = 'ON',
                                             offvalue = 'OFF'
                                             )
        
        frame_1.pack(fill = tk.BOTH, expand=True)
        self.checkbutton_1.pack(pady = 10)


    def status_changed(self):
        status = self.status_var.get()
        print(f'El estado del checkbutton es: {status}')
        
    
if __name__ == '__main__':
    app = Application()
    app.mainloop()
