import tkinter as tk
from tkinter import ttk
from decimal import Decimal

class Application(tk.Tk):
    """Tkinter Application"""
    def __init__(self):
        super().__init__()
        self.title('Calculadora de IVA 1 - Code with Goz')
        self.geometry('450x210')
        # Variables de control
        self.amount_var = tk.StringVar(self)

        # Agregamos un Frame Widget
        main_frame = ttk.Frame(self, padding='10')
        # Creamos un Lable Widget para mostrar instrucciones
        self.instructions_label = ttk.Label(main_frame, text='Escribe una cantidad')
        # Agregamos un Entry Widget ligado a amount_var
        self.amount_entry = ttk.Entry(main_frame, textvariable=self.amount_var, width=15)
        # Creamos un Label Widget para mostrar el resultado
        self.results_label = ttk.Label(main_frame, font=('Arial',18))
        # Creamos un Botón para llamar a la función
        self.button = ttk.Button(main_frame, text='Calcular IVA', command=self.calculate_iva)

    
        # Posicionamos los Widgets en ventana
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.instructions_label.pack(pady=10)
        self.amount_entry.pack(pady=5)
        self.button.pack(pady=10)
        self.results_label.pack(pady=10)

    def calculate_iva(self):
        """Calculates amount's IVA"""
        amount = self.amount_var.get()
        iva = f"${round(Decimal('0.16') * Decimal(amount),2)} M.N."
        self.results_label.config(text=iva)



if __name__ == "__main__":
    app = Application()
    app.mainloop()
