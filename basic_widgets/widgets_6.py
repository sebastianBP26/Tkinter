# Formulario radio buttons

import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    
    def __init__(self):
        ## Tkinter app
        super().__init__()
        self.title('Aprendiendo widgets - Code')
        self.geometry('550x350')

        # Frame Widget
        frame_1 = ttk.Frame(self, padding = '10', borderwidth= 2, relief='sunken')

        # Radio Buttons
        self.language_var = tk.StringVar(value='Python')
        self.radio1 = ttk.Radiobutton(frame_1, 
                                      text='Python', 
                                      variable=self.language_var, 
                                      value='Python',
                                      command = self.show_option)


        self.radio2 = ttk.Radiobutton(frame_1, 
                                      text='Ruby', 
                                      variable=self.language_var, 
                                      value='Ruby',
                                      command = self.show_option)
        
        self.radio3 = ttk.Radiobutton(frame_1, 
                                      text='PHP', 
                                      variable=self.language_var, 
                                      value='PHP',
                                      command = self.show_option)



        frame_1.pack(fill='both', expand=True)
        self.radio1.pack(anchor='w', pady=6)
        self.radio2.pack(anchor='w', pady=6)
        self.radio3.pack(anchor='w', pady=6)


    def show_option(self):
        print(f'Seleccionaste: {self.language_var.get()}')

        
    
if __name__ == '__main__':
    app = Application()
    app.mainloop()