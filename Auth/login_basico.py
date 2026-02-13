# Autenticación Local Básica
import tkinter as tk
from tkinter import ttk, messagebox

import requests

class Application2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Localizador de IP - Code With Goz")
        self.geometry("500x600")

        ############################################################
        # Variables de Control
        ############################################################
        # Creamos una variable de control StringVar
        self.ip_var = tk.StringVar(self)

        ############################################################
        # Widgets
        ############################################################
        # Agregamos un Frame Widget
        main_frame = ttk.Frame(self, padding="10")
        # Creamos un Label Widget para mostrar el resultado
        self.intructions_label = ttk.Label(main_frame, text='Escribe una dirección IP: ')        
        # Agregamos un Entry Widget ligado a ip_var
        self.ip_entry = ttk.Entry(main_frame, textvariable=self.ip_var, width=24)
        # Creamos un Label Widget para mostrar el resultado
        self.results_label = ttk.Label(main_frame, font=("Arial", 18))
        # Creamos un Botón para llamar a la función
        self.button = ttk.Button(main_frame, text="Localizar IP", command=self.locate_ip)

        ############################################################
        # Posicionamos los Widgets en ventana
        ############################################################
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.intructions_label.pack(pady=10)
        self.ip_entry.pack(pady=5)
        self.button.pack(pady=10)
        self.results_label.pack(pady=10)


    def locate_ip(self):
        """Locates IP"""
        ip = self.ip_var.get()

        response = requests.get(f'http://ip-api.com/json/{ip}').json()
        location_data = {
            "ip": ip,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country"),
            "latitude": response.get("lat"),
            "longitude": response.get("lon"),
            "org": response.get("org")
        }
        
        location = f"""
        Dirección IP: {location_data['ip']} 
        Ciudad: {location_data['city']} 
        Región: {location_data['region']} 
        País: {location_data['country']}
        Latitud: {location_data['latitude']} 
        Longitud: {location_data['longitude']} 
        ISP: {location_data['org']}
        """

        self.results_label.config(text=location)
        self.ip_var.set('')

######################################################################################################################################

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Inicio de Sesión') # Título de la ventana
        self.geometry('300x150') # Tamaño de la ventana
        
        # Variables de control
        self.login_var = tk.StringVar(self)
        self.password_var = tk.StringVar(self)

        # Frame
        main_frame = ttk.Frame(self, padding='10')

        # Widgets
        
        ## Login Entry Widget
        self.login_label = ttk.Label(main_frame, text='Usuario: ')
        self.login_entry = ttk.Entry(main_frame, textvariable = self.login_var)
        
        ## Password Entry Widget
        self.password_label = ttk.Label(main_frame, text='Contraseña: ')
        self.password_entry = ttk.Entry(main_frame, textvariable = self.password_var, show='*')

        # Button
        self.button = ttk.Button(main_frame, text='Ingresar', command=self.login)

        # Posicionamos los Widgets en ventana
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.login_label.grid(row = 0, column = 0, padx = 5, pady= 5)
        self.login_entry.grid(row = 0, column = 1, padx=5, pady=5)

        self.password_label.grid(row = 1, column = 0, padx = 5, pady= 5)
        self.password_entry.grid(row = 1, column = 1, padx=5, pady=5)

        self.button.grid(row = 2, column = 0, columnspan = 2, pady=5)

    def login(self):

        """Función para validar el login"""
        login = self.login_var.get()
        password = self.password_var.get()

        if login == 'admin' and password == 'password123':
            messagebox.showinfo('Inicio de Sesión', 'Bienvenido/a')
            app.destroy() # Cerramos la ventana de login
            app2 = Application2()
            app2.mainloop()
        else:
            messagebox.showerror('Inicio de Sesión', 'Usuario o contraseña incorrectos.')

if __name__ == "__main__":
    app = Application()
    app.mainloop()
