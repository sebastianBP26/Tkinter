## En este script agregaremos el tree view para ver en la ventana la base de datos que estamos usando
## El usuario podrá agregar, eliminar y actualizar registros en la base de datos de películas

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
    
    def get_movies(self):
        # Show all movies
        self.cur.execute("SELECT * FROM movies")
        rows = self.cur.fetchall()

        return rows

    def delete_movie(self, id):
        # Delete Movie by id
        self.cur.execute("DELETE FROM movies WHERE id = ?", (id,))
        self.conn.commit()


    def update_movie(self, title, genre, rate, year, format, codebar, price, id):
        """Update Movie"""
        update_query = """
        UPDATE movies SET title = ?, genre = ?, rate = ?,
        year = ?, format = ?, codebar = ?, price = ?
        WHERE id = ?
        """
        self.cur.execute(update_query, (title, genre, rate, year, format, codebar, price, id))
        self.conn.commit()



class Application(tk.Tk):
    
    def __init__(self):
        super().__init__() # Inicializar la clase padre (Tk)
        self.title('Sistema de Gestión de Películas') # Título de la ventana
        self.geometry('1270x750') # Tamaño de la ventana
        self.db = Database(Path.cwd() / 'movies.db') # Archivo tipo SQLite
        
        ###
        ### StringVars: Variables de control
        self.title_var = tk.StringVar(self)
        self.genre_var = tk.StringVar(self)
        self.rate_var = tk.StringVar(self)
        self.year_var = tk.StringVar(self)
        self.format_var = tk.StringVar(self)
        self.codebar_var = tk.StringVar(self)
        self.price_var = tk.StringVar(self)

        ### Widgets
        main_frame = ttk.Frame(self, padding = 10)
        self.instructions_label = ttk.Label(main_frame, text = 'Completa el formulario para agregar una nueva película')
        
        ### Title
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
        self.delete_button = ttk.Button(main_frame, text = 'ELIMINAR', command= self.delete_movie)
        self.update_button = ttk.Button(main_frame, text = 'ACTUALIZAR', command= self.update_movie)

        ## Tree view Widget:
        self.tree_view = ttk.Treeview(main_frame,  # En dónde va a exisitr
                                      columns = ('id', 'title', 'genre', 'rate', 'year', 'format', 'codebar', 'price'), # Columnas a mostrar
                                      show = 'headings' # Mostrar solo los encabezados de las columnas
                                      )
        ## Definimos los columns headings
        self.tree_view.heading('id', text = 'ID')
        self.tree_view.heading('title', text = 'Título')
        self.tree_view.heading('genre', text = 'Género')
        self.tree_view.heading('rate', text = 'Rate')
        self.tree_view.heading('year', text = 'Año')
        self.tree_view.heading('format', text = 'Formato')
        self.tree_view.heading('codebar', text = 'Barcode')
        self.tree_view.heading('price', text = 'Precio')

        ## Definimos los anchos
        self.tree_view.column('id', width = 3)
        self.tree_view.column('title', width = 250)
        self.tree_view.column('genre', width = 30)
        self.tree_view.column('rate', width = 15)
        self.tree_view.column('year', width = 25)
        self.tree_view.column('format', width = 20, anchor = tk.E)
        self.tree_view.column('codebar', width = 50, anchor= tk.E)
        self.tree_view.column('price', width = 25, anchor = tk.E)

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
        self.button.pack(pady = 15)
        self.delete_button.pack(pady = 10)
        self.update_button.pack(pady = 10)
        self.results_label.pack(pady = 10)

        # Create a vertical Scrollbar
        v_scrollbar = ttk.Scrollbar(main_frame, 
                                    orient = tk.VERTICAL, # Posición del scrollbar
                                    command=self.tree_view.yview # Función que se ejecuta al mover el scrollbar, en este caso, el método yview del tree view
                                    )
        # Posicionamiento
        self.tree_view.configure(yscrollcommand=v_scrollbar.set) # Se necesita para agregarlo al tree view
        self.tree_view.pack(fill = tk.BOTH, expand = True, side = tk.LEFT)
        v_scrollbar.pack(fill = tk.Y, side = tk.RIGHT) # Posicionamiento del scrollbar, se pone al lado derecho del tree view

        self.populate_my_table()
        self.tree_view.bind('<<TreeviewSelect>>', self.on_tree_select) # Evento que se ejecuta al seleccionar un elemento del tree view, se llama al método on_tree_select


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
            self.clean_table()
            self.populate_my_table()

    def delete_movie(self):
        select_item = self.tree_view.focus()
        item_details = self.tree_view.item(select_item)
        
        self.db.delete_movie(item_details['values'][0])
        self.results_label.config(text = 'La película fue eliminada de la Base de Datos')
        self.reset_fields()
        self.clean_table()
        self.populate_my_table()

    def update_movie(self):
        select_item = self.tree_view.focus()
        item_details = self.tree_view.item(select_item)

        title = self.title_var.get()
        genre = self.genre_var.get()
        rate = self.rate_var.get()
        year = self.year_var.get()
        format = self.format_var.get()
        barcode = self.codebar_var.get()
        price = self.price_var.get()
        id = item_details['values'][0]

        self.db.update_movie(title, genre, rate, year, format, barcode, price, id)
        self.results_label.config(text = 'La película fue actualizada en la Base de Datos')
        self.reset_fields()
        self.clean_table()
        self.populate_my_table()



    def populate_my_table(self):
        for row in self.db.get_movies():
            print(row)
            self.tree_view.insert('', tk.END, values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    
    def validate_fields(self, title, genre, rate, year, format, barcode, price):
        
        ## Validate from fields
        if title == '' or genre == '' or rate == '' or year == '' or barcode == '' or price == '' or format == '':
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

    def clean_table(self):
        """ Clean tree view table """
        children_ids = self.tree_view.get_children()
        self.tree_view.delete(*children_ids)

    def on_tree_select(self, event):
        """Evento que se ejecuta al seleccionar un elemento del tree view"""
        selected_item = self.tree_view.focus()
        item_details = self.tree_view.item(selected_item)
        try:
            item_values = item_details['values']
            self.title_var.set(item_values[1])
            self.genre_var.set(item_values[2])
            self.rate_var.set(item_values[3])
            self.year_var.set(item_values[4])
            self.format_var.set(item_values[5])
            self.codebar_var.set(item_values[6])
            self.price_var.set(item_values[7])
        except:
            pass
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()  