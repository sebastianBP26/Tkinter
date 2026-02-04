# Formulario con varios frame widgets y organizados con grid

# Formulario básico con Frame widgets

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Application(tk.Tk):
    
    def __init__(self):
        ## Tkinter app
        super().__init__()
        self.title('Aprendiendo widgets - Code')
        self.geometry('1026x650')

        # Frame Widget
        # Label
        frame_1 = ttk.Frame(self, padding='10')
        # Podemos mostrar texto
        self.text_label = ttk.Label(frame_1, text='Soy el Label 1')

        # Podemos mostrar imágenes utilizando pillow
        pil_image = Image.open('image.png')
        tk_image = ImageTk.PhotoImage(pil_image)
        self.image_label = ttk.Label(frame_1, image=tk_image)

        # Posicionamos los widgets en la ventana
        frame_1.pack(fill = tk.BOTH, expand = True)
        self.text_label.pack(pady = 10)
        self.image_label.pack(pady=10)

        # Importante: Mantener la referencia a las imágenes
        self.image_label.image = tk_image

        ## Imagen a la izquierda del texto
        pil_image2 = Image.open('image.png')
        tk_image2 = ImageTk.PhotoImage(pil_image2)
        self.image_label2 = ttk.Label(frame_1, 
                                      image=tk_image2, 
                                      compound='left', 
                                      text = 'Este es un Label con imagen y texto')
        
        self.image_label2.pack(pady=10)
        self.image_label2.image = tk_image2

        ##
        self.anchor_label = ttk.Label(frame_1, 
                                      text='Soy el ancho',
                                      anchor = 's',
                                      width = 52,
                                      background='lightblue')
        self.anchor_label.pack(pady=10)




if __name__ == '__main__':
    app = Application()
    app.mainloop()
