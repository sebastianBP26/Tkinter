# Modules
from tkinter import *
import csv
from datetime import datetime
from decimal import Decimal as D
from pathlib import Path

def check_file_presence():
    """ Check CSV file presence """
    csv_path = Path.cwd() / 'ventas.csv'
    if not csv_path.exists():
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            file = csv.writer(f)
            file.writerow(['Producto','Precio','Cantidad','Total','Día','Hora'])


def add_item():
    """ Adds item to sales report """
    csv_path = Path.cwd() / 'ventas.csv'

    product_name = product_var.get().capitalize()
    product_price = D(price_var.get())
    product_quantity = int(quantity_var.get())
    total = product_price * product_quantity
    current_date = datetime.now().strftime("%D")
    current_time = datetime.now().strftime("%H:%M:%S")
    message_label["text"] = f'''
    Último producto vendido:

    {product_name}
    Precio: ${product_price} M.N.
    Cantidad: {product_quantity}
    Total: ${total} M.N.
    {current_date}
    {current_time} 
    '''
    clear_text()
    # Agregamos información a un csv
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        file = csv.writer(f)
        file.writerow([product_name, product_price, product_quantity, total, current_date, current_time])

def clear_text():
    """ Clear form """
    product_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)


window = Tk()
window.title("Registro de ventas - Sebastian' Store")


# Agregamos etiquetas y campo de entrada
product_label = Label(window, text='Nombre del producto:')
product_var = StringVar()
product_entry = Entry(window, textvariable=product_var, width=30)

price_label = Label(window, text='Precio:')
price_var = StringVar()
price_entry = Entry(window, textvariable=price_var, width=30)

quantity_label = Label(window, text='Cantidad:')
quantity_var = StringVar()
quantity_entry = Entry(window, textvariable=quantity_var, width=30)

# Agregamos widgets de texto para mostrar mensajes
message_label = Label(window, height=8, width=30, font=('Arial',15))

# Agregamos el botón
button = Button(window, text='AGREGAR PRODUCTO', command=add_item)

# Indicamos dónde se colocarán los widgets
# utilizando pack (geometry package method)
product_label.pack()
product_entry.pack()
price_label.pack()
price_entry.pack()
quantity_label.pack()
quantity_entry.pack()
button.pack()
message_label.pack()

# Iniciamos la interfaz gráfica
window.mainloop()