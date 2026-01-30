import tkinter as tk
from tkinter import ttk
from decimal import Decimal

class Application(tk.Tk):
    """Tkinter Application"""
    def __init__(self):
        super().__init__()
        self.title('Calculadora de IVA 1 - Code with Goz')
        self.geometry('450x250')
        # Variables de control
        self.amount_var = tk.StringVar(self)

        # Agregamos un Frame Widget
        main_frame = ttk.Frame(self, padding='10')
        # Creamos un Lable Widget para mostrar instrucciones
        self.instructions_label = ttk.Label(main_frame, text='Escribe una cantidad')
        # Agregamos un Entry Widget ligado a amount_var
        self.amount_entry = ttk.Entry(main_frame, textvariable=self.amount_var, width=15)
        # Creamos Label Widgets para mostrar los resultados
        self.amount_label = ttk.Label(main_frame, font=('Arial',12))
        self.iva_label = ttk.Label(main_frame, font=('Arial',12))
        self.total_label = ttk.Label(main_frame, font=('Arial',12))
        # Creamos un Botón para llamar a la función
        self.button = ttk.Button(main_frame, text='Calcular IVA', command=self.calculate_iva)

    
        # Posicionamos los Widgets en ventana
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.instructions_label.pack(pady=10)
        self.amount_entry.pack(pady=5)
        self.button.pack(pady=10)
        self.amount_label.pack(pady=5)
        self.iva_label.pack(pady=5)
        self.total_label.pack(pady=5)


    def calculate_iva(self):
        try:
            """Calculates amount's IVA"""
            amount = self.amount_var.get()
            iva = round(Decimal('0.16') * Decimal(amount),2)
            total = Decimal(amount) + iva
            self.amount_label.config(text=f'Cantidad: ${amount} M.N.')
            self.iva_label.config(text=f'IVA: ${iva} M.N.')
            self.total_label.config(text=f'Total: ${total} M.N.')
        
        except:
            self.amount_label.config(text = 'El valor ingresado no es válido')
            self.iva_label.config(text = '')
            self.total_label.config(text = '')


if __name__ == "__main__":
    app = Application()
    app.mainloop()


