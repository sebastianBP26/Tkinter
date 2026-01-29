# Modules
import tkinter as tk

# Window
root = tk.Tk()

# Att Window
root.title('Mi primer GUI')
root.geometry('370x260')

# Entries
label = tk.Label(root, text = 'Hola Mundo!!')
entry = tk.Entry(root, text = '')
buttom = tk.Button(root, text = 'Entrar')

# Indicamos dónde se colocarán los widgets
label.pack()
entry.pack()
buttom.pack()

## Iniciamos la ventana
root.mainloop()