import tkinter as tk
from tkinter import ttk
from pathlib import Path
from datetime import datetime
import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor() # Cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title, genre, rate, year, format, codebar, price)")
        self.conn.commit()

    def insert(self, title, genre, rate, year, format, codebar, price):
        
        title = self.sanitize_field(title)
        genre = self.sanitize_field(genre)
        rate = self.sanitize_field(rate)
        year = self.sanitize_field(year)
        format = self.sanitize_field(format)
        codebar = self.sanitize_field(codebar)
        price = self.sanitize_field(price)

        self.cur.execute("INSERT INTO movies VALUES (NULL,?,?,?,?,?,?,?)", (title, genre, rate, year, format, codebar, price))
        self.conn.commit()


    def sanitize_field(self, field):
        """Sanitize input field"""
        field = field.replace(';','').replace('DELETE','').replace('UPDATE','').replace('CREATE','')
        return field


class Application(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Sistema de Gestión de Películas')
        self.geometry('800x600')
        self.db = Database(Path.cwd() / 'movies.db') # Archivo tipo SQLite
        
        # StringVars: Variables de control
        self.title_var = tk.StringVar(self)
        self.genre_var = tk.StringVar(self)
        self.rate_var = tk.StringVar(self)
        self.year_var = tk.StringVar(self)
        self.format_var = tk.StringVar(self)
        self.codebar_var = tk.StringVar(self)
        self.price_var = tk.StringVar(self)

        # Widgets
        main_frame = ttk.Frame(self, padding = 10)
        self.instructions_label = ttk.Label(main_frame, text = 'Completa el formulario para agregar una nueva película')
        
        # Title
        self.title_label = ttk.Label(main_frame, text = 'Título:')
        self.title_entry = ttk.Entry(main_frame, textvariable = self.title_var, width=35)

        # Género
        self.genre_label = ttk.Label(main_frame, text = 'Género:')
        self.genre_combo = ttk.Combobox(main_frame, 
                                        textvariable = self.genre_var, 
                                        values = ['Acción', 'Comedia', 'Suspenso', 'Romance', 'Infantil'], 
                                        width = 15
                                        )
        
        # Rate
        self.rate_label = ttk.Label(main_frame, text = 'Rate:')
        self.rate_combo = ttk.Combobox(main_frame, 
                                        textvariable = self.rate_var, 
                                        values = ['A', 'B', 'C', 'D', 'R'], 
                                        width = 3
                                        )
        
        # year
        self.year_label = ttk.Label(main_frame, text = 'Año:')
        actual_year = datetime.now().year + 1
        year_list = list(range(1970, actual_year))
        self.year_combo = ttk.Combobox(main_frame, textvariable=self.year_var, values = year_list, width=8)

        # Formato
        self.format_label = ttk.Label(main_frame, text = 'Formato: ')
        self.format_combo = ttk.Combobox(main_frame, textvariable=self.format_var, values = ['Bluray', 'DVD', 'VHS', 'Digital'], width=8)

        # Barcode
        self.codebar_label = ttk.Label(main_frame, text = 'Barcode:')
        self.codebar_entry = ttk.Entry(main_frame, textvariable= self.codebar_var, width = 26)

        # Price
        self.price_label = ttk.Label(main_frame, text = 'Precio:')
        self.price_entry = ttk.Entry(main_frame, textvariable=self.price_var, width= 15)

        # Resultados
        self.results_label = ttk.Label(main_frame)
    
        # Botón de acción
        self.button = ttk.Button(main_frame, text = 'AGREGAR', command= self.add_movie)

        ##### Posicionamiento
        main_frame.pack(fill = tk.BOTH, expand = True)
        self.instructions_label.pack(pady = 10)
        # Title
        self.title_label.pack(pady = 3)
        self.title_entry.pack(pady = 5)

        # Genre
        self.genre_label.pack(pady = 3)
        self.genre_combo.pack(pady = 5)

        # Rate
        self.rate_label.pack(pady=3)
        self.rate_combo.pack(pady=5)

        # Year
        self.year_label.pack(pady=3)
        self.year_combo.pack(pady = 5)

        # Formato
        self.format_label.pack(pady=3)
        self.format_combo.pack(pady=5)

        # Barcode
        self.codebar_label.pack(pady=3)
        self.codebar_entry.pack(pady=5)

        # Price
        self.price_label.pack(pady=3)
        self.price_entry.pack(pady=5)

        # Botón
        self.button.pack(pady = 25)
        self.results_label.pack(pady = 18)


    def add_movie(self):
        """ Agregar película a la base de datos"""

        # Valores de entrada
        title = self.title_var.get()
        genre = self.genre_var.get()
        rate = self.rate_var.get()
        year = self.year_var.get()
        format = self.format_var.get()
        barcode = self.codebar_var.get()
        price = self.price_var.get()

        if self.validate_fields(title, genre, rate, year, format, barcode, price):
            self.db.insert(title, genre, rate, year, format, barcode, price)
            self.results_label.config(text = 'La película fue agregada a la Base de Datos')
            self.reset_fields()

    
    def validate_fields(self, title, genre, rate, year, format, barcode, price):
        
        ## Validate from fields
        if title == '' or genre == '' or rate == '' or year == '' or barcode == '' or price == '':
            validation = False
        else:
            validation = True
        
        return validation
    
    def reset_fields(self):
        """Reset form fields"""
        self.title_var.set('')
        self.genre_var.set('')
        self.rate_var.set('')
        self.year_var.set('')
        self.format_var.set('')
        self.codebar_var.set('')
        self.price_var.set('')

        

if __name__ == '__main__':
    app = Application()
    app.mainloop()  