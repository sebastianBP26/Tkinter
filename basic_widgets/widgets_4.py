# Formulario básico con Frame widgets

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Application(tk.Tk):
    
    def __init__(self):
        ## Tkinter app
        super().__init__()
        self.title('Aprendiendo widgets - Code')
        self.geometry('1026x840')

        # Frame Widget
        frame_1 = ttk.Frame(self, padding = '10')
        
        # Button Widget: Puede desplegar texto o imágenes
        
        ## Botón clásico con texto
        self.button = ttk.Button(frame_1, 
                                 text = 'Botón 1', 
                                 command = self.say_hello_1)

        ## Botón con imagen
        pil_image = Image.open('image.png')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.button2 = ttk.Button(frame_1, 
                                  image = tk_image, 
                                  command = self.say_hello_2)

        ## 
        pil_image2 = Image.open('image.png')
        tk_image2 = ImageTk.PhotoImage(pil_image2)
        self.button3 = ttk.Button(frame_1, 
                                  image = tk_image2, 
                                  command = self.say_hello_3,
                                  text = 'Botón 3', 
                                  compound = 'right')
        
        ## 
        self.button4 = ttk.Button(frame_1, 
                                  text = 'Botón 4',
                                  command = self.say_hello_4)
        self.bind('<Key-Return>', lambda e: self.button4.invoke())

        ## Asociado a ESC
        self.button5 = ttk.Button(frame_1, 
                                  text = 'Botón 5',
                                  command = self.say_hello_5)
        self.bind('<Key-Escape>', lambda e: self.button5.invoke())

        ## Botón estado disable
        self.button6 = ttk.Button(frame_1, 
                                  text = 'Botón 6',
                                  command = self.say_hello_5)
        self.button6.state(['disabled'])

        
        # Referencia
        self.button2.image = tk_image
        self.button3.image = tk_image2

        # Posicionamiento
        frame_1.pack(fill = tk.BOTH, expand=True)
        self.button.pack(pady = 26)
        self.button2.pack(pady = 26)
        self.button3.pack(pady = 26)
        self.button4.pack(pady = 26)
        self.button5.pack(pady = 26)
        self.button6.pack(pady = 26)
        

    def say_hello_1(self):
        print('Hola desde el botón 1')

    def say_hello_2(self):
        print('Hola desde el botón 2')

    def say_hello_3(self):
        print('Hola desde el botón 3')
    
    def say_hello_4(self):
        print('Hola desde el botón 4')

    def say_hello_5(self):
        print('Hola desde el botón 5')

    
if __name__ == '__main__':
    app = Application()
    app.mainloop()
