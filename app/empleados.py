import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import socket
import sqlite3

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("e-StockTag Admin Panel")
        self.geometry("768x540")

        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure((1, 2,3,4,5), weight=0)

        # Create sidebar frame with widgets. FRAME LEFT BOX
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")

        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="e-StockTag", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=40, pady=(20, 10))

        #This button should display when clicked the FRAME AGREGAR TRABAJADOR inside the FRAME RIGHT BOX
        self.sidebar_button = ctk.CTkButton(self.sidebar_frame, text="Registrar empleado")
        self.sidebar_button.grid(row=1, column=0, padx=40, pady=10)

        self.sidebar_button1 = ctk.CTkButton(self.sidebar_frame, text="Ver empleados")
        self.sidebar_button1.grid(row=2, column=0, padx=40, pady=10)

        # Main content area. FRAME RIGHT BOX. this frame is like a div where all other frames are going to be loaded when their corresponding button is clicked
        # This would be FRAME AGREGAR TRABAJADOR
        self.label_1 = ctk.CTkLabel(self, text="Ingresar datos del trabajador",font=ctk.CTkFont(size=20,weight="bold"))
        self.label_1.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.entry = ctk.CTkEntry(self, placeholder_text="Nombre",width=350)
        self.entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        self.string_input_button_2 = ctk.CTkEntry(self, placeholder_text="Apellido Materno",width=350)
        self.string_input_button_2.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        self.string_input_button_3 = ctk.CTkEntry(self, placeholder_text="Apellido Paterno",width=350)
        self.string_input_button_3.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        self.string_input_button_4 = ctk.CTkEntry(self, placeholder_text="Linea de trabajo",width=350)
        self.string_input_button_4.grid(row=4, column=1, padx=20, pady=20, sticky="w")
        
        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Agregar trabajador",command=self.sidebar_button_event)
        self.main_button_1.grid(row=5, column=1, padx=(20, 20), pady=70, sticky="w")

        #This part of the code would be the FRAME VER TRABAJADORES.
        self.tabla = tk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla.column('Modelo', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Precio', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Codigo', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Modelo', text='Modelo', anchor ='center')
        self.tabla.heading('Precio', text='Precio', anchor ='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor ='center')


        estilo = tk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila

        
        
        

    def sidebar_button_event(self):
        # Conectarse a la base de datos y registrar los datos
        
        nombre = self.entry.get()
        apellido_materno = self.string_input_button_2.get()
        apellido_paterno = self.string_input_button_3.get()
        linea = self.string_input_button_4.get()
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trabajador (nombre, apellidoM, apellidoP, linea)
                VALUES (?, ?, ?, ?)
            """, (nombre, apellido_materno, apellido_paterno, linea))
            conn.commit()
            conn.close()
            messagebox.showinfo("Exito","Se ingreso al nuevo trabajador exitosamente")
        except Exception as e:
            messagebox.showerror("Error",e)

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    


 