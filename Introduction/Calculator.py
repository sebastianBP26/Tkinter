# Modules
from tkinter import *
from decimal import Decimal as D

# Root window
window = Tk()

# Configuration
window.title('Currency Convertor')
window.geometry('370x370')

# Funciones
def convert_pesos():
    pesos = D(amount_var.get())

    # Fix values
    dollars = '$ ' + str(round(pesos / D('17.8'),2))
    euros = '€ ' + str(round(pesos / D('19.8'),2))
    yens = '¥ ' + str(round(pesos / D('0.14'),2))

    result1_label['text'] = dollars
    result2_label['text'] = euros
    result3_label['text'] = yens

# Input Labels & Fields
instructions_label = Label(window, text = 'How much mexican pesos do you have?')
amount_var = StringVar()
amount_entry = Entry(window, textvariable=amount_var)
dollar_label = Label(window, text = 'Dolars')
euro_label = Label(window, text = 'Euros')
yen_label = Label(window, text = 'Yens')

# Widgets
result1_label = Label(window, height=1, width=20, font = ('Arial', 12))
result2_label = Label(window, height=1, width=20, font = ('Arial', 12))
result3_label = Label(window, height=1, width=20, font = ('Arial', 12))

# Button
button = Button(window, text = 'Convert', command = convert_pesos)

# Locate
instructions_label.pack()
amount_entry.pack()
button.pack()

yen_label.pack()
result3_label.pack()

euro_label.pack()
result2_label.pack()

dollar_label.pack()
result1_label.pack()

# Initialice Window
window.mainloop()