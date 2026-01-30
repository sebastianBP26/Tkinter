# Se cambian widgets

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import csv
from datetime import datetime

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Movies')
        self.geometry('450x800')

        # Variables de control
        self.title_var = tk.StringVar(self)
        self.genre_var = tk.StringVar(self)
        self.rate_var = tk.StringVar(self)
        self.year_var = tk.StringVar(self)
        self.format_var = tk.StringVar(self)
        self.price_var = tk.StringVar(self)

        # Add frame - Widget
        main_frame = ttk.Frame(self, padding = 10)
        # Creamos label widget
        self.instructions_label = ttk.Label(main_frame, 
                                            text = '¡Completa el formulario para agregar una nueva película!')
        
        # Entry widgets
        self.title_label = ttk.Label(main_frame, text = 'Título:')
        self.title_entry = ttk.Entry(main_frame, textvariable= self.title_var, width= 35)

        self.genre_label = ttk.Label(main_frame, text = 'Género:')
        # self.genre_entry = ttk.Entry(main_frame, textvariable= self.genre_var, width= 15)
        self.genre_combo = ttk.Combobox(main_frame,
                                        textvariable=self.genre_var,
                                        values = ['acción', 'comedia', 'romance', 'terror', 'suspenso', 'infantil'],
                                        width= 15)
        
        self.rate_label = ttk.Label(main_frame, text = 'Clasificación:')
        # self.rate_entry = ttk.Entry(main_frame, textvariable= self.rate_var, width= 15)
        self.rate_combo = ttk.Combobox(main_frame,
                                        textvariable=self.rate_var,
                                        values = ['A', 'B', 'C', 'D', 'R', 'XXX'],
                                        width= 3)
        

        self.year_label = ttk.Label(main_frame, text = 'Año')
        # self.year_entry = ttk.Entry(main_frame, textvariable= self.year_var, width= 15)
        actual_year = datetime.now().year + 1 # Este año + 1
        year_list = list(range(1970, actual_year)) # Rango de 1970 hasta el año actual, por eso el +1
        self.year_combo = ttk.Combobox(main_frame,
                                        textvariable=self.year_var,
                                        values = year_list,
                                        width = 5 
                                      )
        

        self.format_label = ttk.Label(main_frame, text = 'Formato')
        # self.format_entry = ttk.Entry(main_frame, textvariable= self.format_var, width= 15)
        self.format_combo = ttk.Combobox(main_frame,
                                        textvariable=self.format_var,
                                        values = ['Bluray', 'DVD', 'VHS', 'Digital'],
                                        width= 8)
        

        self.price_label = ttk.Label(main_frame, text = 'Precio')
        self.price_entry = ttk.Entry(main_frame, textvariable= self.price_var, width= 15)

        # Label widget para mostrar resultado
        self.result_label = ttk.Label(main_frame)

        # Botón para llamar a la función
        self.button = ttk.Button(main_frame, text = 'Agregar Película', command = self.add_movie)

        # Posicionar widgets
        main_frame.pack(fill = tk.BOTH, expand= True)
        self.instructions_label.pack(pady = 10)
        
        self.title_label.pack(pady = 3)
        self.title_entry.pack(pady = 5)

        self.genre_label.pack(pady = 3)
        self.genre_combo.pack(pady = 5)

        self.rate_label.pack(pady = 3)
        self.rate_combo.pack(pady = 5)

        self.year_label.pack(pady = 3)
        self.year_combo.pack(pady = 5)

        self.format_label.pack(pady = 3)
        self.format_combo.pack(pady = 5)

        self.price_label.pack(pady = 3)
        self.price_entry.pack(pady = 5)

        self.button.pack(pady = 25)
        self.result_label.pack(pady = 10)


    def add_movie(self):
        # Funcion para "agregar" la película
        title = self.title_var.get()
        genre = self.genre_var.get()
        rate = self.rate_var.get()
        year = self.year_var.get()
        format = self.format_var.get()
        price = self.price_var.get()

        # Ruta al archivo
        my_csv_path = Path.cwd() / 'movies.csv'

        with open(my_csv_path, 'a') as file:
            writer = csv.writer(file, delimiter=",", quotechar = '"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([title, genre, rate, year, format, price]) # Variables obtenidas

        message = f'''
        {title} ({year}) de género {genre} 
        y clasificación {rate} en formato {format}
        fue agregagada al archivo.
        '''
        self.result_label.config(text = message)

        self.title_var.set('')
        self.genre_var.set('')
        self.rate_var.set('')
        self.year_var.set('')
        self.format_var.set('')
        self.price_var.set('')

if __name__ == "__main__":
    app = Application()
    app.mainloop()