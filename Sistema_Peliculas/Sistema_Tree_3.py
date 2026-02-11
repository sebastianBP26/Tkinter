import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title, genre, rate, year, format, codebar, price)")
        self.conn.commit()

    def insert(self, title, genre, rate, year, format, codebar, price):
        title = self.sanitize_field(title)
        genre = self.sanitize_field(genre)
        rate = self.sanitize_field(rate)
        year = self.sanitize_field(year)
        format = self.sanitize_field(format)
        codebar = self.sanitize_field(codebar)
        self.cur.execute("INSERT INTO movies VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (title, genre, rate, year, format, codebar, price))
        self.conn.commit()

    def sanitize_field(self, field):
        """Sanitize input field"""
        field = field.replace(';','').replace('DELETE','').replace('UPDATE','').replace('CREATE','')
        return field
    
    def get_movies(self):
        """Show all movies"""
        self.cur.execute("SELECT * FROM movies ORDER BY year")
        rows = self.cur.fetchall()
        return rows

    def delete_movie(self, id):
        """Delete movie"""
        self.cur.execute("DELETE FROM movies WHERE id = ?", (id,))
        self.conn.commit()

    def update_movie(self, title, genre, rate, year, format, codebar, price, id):
        """Update movie"""
        update_query = """
        UPDATE movies SET title = ?, genre = ?, rate = ?, 
        year = ?, format = ?, codebar = ?, price = ? 
        WHERE id = ? 
        """
        self.cur.execute(update_query, (title, genre, rate, year, format, codebar, price, id))
        self.conn.commit()



###############################################################
# Curso Tkinter Python (Code With Goz)
# Sistema de Películas 3
# Objetivo: Entender CRUD con conexión a DB 
# y agregando Treeview y Grid
# Autor: Goz
###############################################################

import tkinter as tk
from tkinter import ttk
from pathlib import Path
from datetime import datetime


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mis Películas - Code With Goz")
        self.geometry("1270x750")
        self.db = Database(Path.cwd() / 'movies.db')

        ############################################################
        # Variables de Control
        ############################################################
        # Creamos una variable de control IntVar
        self.title_var = tk.StringVar(self)
        self.genre_var = tk.StringVar(self)
        self.rate_var = tk.StringVar(self)
        self.year_var = tk.StringVar(self)
        self.format_var = tk.StringVar(self)
        self.price_var = tk.IntVar(self)
        self.barcode_var = tk.StringVar(self)


        ############################################################
        # Widgets
        ############################################################
        # Agregamos un Frame Widget
        top_frame = ttk.Frame(self)
        top_frame.pack(side=tk.TOP, pady=25)

        main_frame = ttk.Frame(self)
        main_frame.pack(side=tk.TOP)

        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=26)
        
        # Creamos un Label Widget con las instrucciones:
        self.intructions_label = ttk.Label(top_frame, text='Completa el formulario para agregar una película: ')        
        self.intructions_label.pack(pady=0)

        # Agregamos los Entry Widgets ligados a las variables de control
        self.title_label = ttk.Label(main_frame, text='Titulo: ')        
        self.title_label.grid(row=0, column=0, padx=15, pady=25)

        self.title_entry = ttk.Entry(main_frame, textvariable=self.title_var, width=48)
        self.title_entry.grid(row=0, column=1, padx=0, pady=25)

        self.genre_label = ttk.Label(main_frame, text='Género: ')
        self.genre_label.grid(row=0, column=2, padx=10, pady=25)

        self.genre_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.genre_var, 
            values=[
                'acción', 'aventura', 'ciencia ficción', 'comedia', 'drama', 
                'terror', 'fantasía', 'musical', 'romance', 'suspenso',
                'western', 'animación', 'bélico', 'biográfico', 'documental',
                'crimen/policiaco', 'deportes', 'histórico'
                ], 
            width=15)
        self.genre_combo.grid(row=0, column=3, padx=0, pady=25)

        self.rate_label = ttk.Label(main_frame, text='Clasificación: ')
        self.rate_label.grid(row=0, column=4, padx=10, pady=25)

        self.rate_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.rate_var, 
            values=['G','PG','PG-13','R','NC-17'], 
            width=10)
        self.rate_combo.grid(row=0, column=5, padx=0, pady=25)
        
        self.year_label = ttk.Label(main_frame, text='Año: ')
        self.year_label.grid(row=0, column=6, padx=10, pady=25)

        actual_year = datetime.now().year + 1
        year_list = list(range(1970, actual_year))
        self.year_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.year_var, 
            values=year_list,
            width=5)
        self.year_combo.grid(row=0, column=7, padx=0, pady=25)
                        
        self.format_label = ttk.Label(main_frame, text='Formato: ')
        self.format_label.grid(row=0, column=8, padx=10, pady=25)
        self.format_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.format_var, 
            values=['Bluray','DVD'],
            width=8)
        self.format_combo.grid(row=0, column=9, padx=0, pady=25)
        
        self.barcode_label = ttk.Label(main_frame, text='Código: ')
        self.barcode_label.grid(row=1, column=0, padx=10, pady=5)
        self.barcode_entry = ttk.Entry(main_frame, textvariable=self.barcode_var, width=48)
        self.barcode_entry.grid(row=1, column=1, padx=10, pady=5)

        self.price_label = ttk.Label(main_frame, text='Precio: ')
        self.price_label.grid(row=1, column=2, padx=10, pady=5)
        self.price_entry = ttk.Entry(main_frame, textvariable=self.price_var, width=8)
        self.price_entry.grid(row=1, column=3, padx=0, pady=5)


        # Creamos un Label Widget para mostrar el resultado
        self.results_label = ttk.Label(main_frame)
        self.results_label.grid(row=1, column=4, padx=0, pady=5, columnspan=5)


        # Creamos un Botón para llamar a la función
        self.button = ttk.Button(main_frame, text="AGREGAR", command=self.add_movie)
        self.button.grid(row=3, column=0, padx=0, pady=20, columnspan=2)

        self.delete_button = ttk.Button(main_frame, text="ELIMINAR", command=self.delete_movie)
        self.delete_button.grid(row=3, column=4, padx=0, pady=20, columnspan=2)

        self.update_button = ttk.Button(main_frame, text="ACTUALIZAR", command=self.update_movie)
        self.update_button.grid(row=3, column=7, padx=0, pady=20, columnspan=2)


        # Define the Treeview with columns
        self.treeview = ttk.Treeview(bottom_frame, columns=(
                "id",
                "title", 
                "genre",  
                "rate",
                "year", 
                "format", 
                "barcode",
                "price"
            ), 
            show="headings"
        )

        # Define column headings
        self.treeview.heading("id", text="Id")
        self.treeview.heading("title", text="Título")
        self.treeview.heading("genre", text="Género")
        self.treeview.heading("rate", text="Clasificación")
        self.treeview.heading("year", text="Año")
        self.treeview.heading("format", text="Formato")
        self.treeview.heading("barcode", text="Código de Barras")
        self.treeview.heading("price", text="Precio")

        # Define column widths
        self.treeview.column("id", width=3)
        self.treeview.column("title", width=250)
        self.treeview.column("genre", width=30)
        self.treeview.column("rate", width=15)
        self.treeview.column("year", width=25)
        self.treeview.column("format", width=20, anchor=tk.E)
        self.treeview.column("barcode", width=50, anchor=tk.E)        
        self.treeview.column("price", width=25, anchor=tk.E)        

        ############################################################
        # Posicionamos los Widgets en ventana
        ############################################################


        # Create a vertical scrollbar
        v_scrollbar = ttk.Scrollbar(bottom_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=v_scrollbar.set)

        # Pack the Treeview and scrollbar
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.populate_my_table()
        self.treeview.bind('<<TreeviewSelect>>', self.on_tree_select)



    def add_movie(self):
        """Add movie to Database"""
        title = self.title_var.get()
        genre = self.genre_var.get()
        rate = self.rate_var.get()
        year = self.year_var.get()
        format = self.format_var.get()
        barcode = self.barcode_var.get()
        price = self.price_var.get()

        if self.validate_fields(title, genre, rate, year, format, barcode, price):

            self.db.insert(title, genre, rate, year, format, barcode, price)
            
            self.results_label.config(text='La Película fue agregada a la Base de Datos!!!')
            self.reset_fields()
            self.clean_my_table()
            self.populate_my_table()

        else:
            self.results_label.config(text='Debes completar todos los campos!!!')


    def validate_fields(self, title, genre, rate, year, format, barcode, price):
        """Validate form fields"""
        if title == '' or genre == '' or rate == '' or year == '' or format == '' or barcode == '' or price == '':
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
        self.barcode_var.set('')
        self.price_var.set('')

    def populate_my_table(self):
        for row in self.db.get_movies():
            print(row)
            self.treeview.insert("", tk.END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

    def clean_my_table(self):
        children_ids = self.treeview.get_children()
        self.treeview.delete(*children_ids)

    def on_tree_select(self, event):
        selected_item = self.treeview.focus()
        item_details = self.treeview.item(selected_item)
        try:
            self.title_var.set(item_details['values'][1])
            self.genre_var.set(item_details['values'][2])
            self.rate_var.set(item_details['values'][3])
            self.year_var.set(item_details['values'][4])
            self.format_var.set(item_details['values'][5])
            self.barcode_var.set(item_details['values'][6])
            self.price_var.set(item_details['values'][7])
        except:
            pass
     

    def delete_movie(self):
        selected_item = self.treeview.focus()
        item_details = self.treeview.item(selected_item)
        self.db.delete_movie(item_details['values'][0])
        self.results_label.config(text='La Película fue eliminada de la Base de Datos!!!')
        self.reset_fields()
        self.clean_my_table()
        self.populate_my_table()  

    def update_movie(self):
        selected_item = self.treeview.focus()
        item_details = self.treeview.item(selected_item)

        title = self.title_var.get()
        genre = self.genre_var.get()
        rate = self.rate_var.get()
        year = self.year_var.get()
        format = self.format_var.get()
        barcode = self.barcode_var.get()
        price = self.price_var.get()
        id = item_details['values'][0]

        self.db.update_movie(title, genre, rate, year, format, barcode, price, id)
        self.results_label.config(text='La Película fue actualizada en la Base de Datos!!!')
        self.reset_fields()
        self.clean_my_table()
        self.populate_my_table()  


if __name__ == "__main__":
    app = Application()
    app.mainloop()





