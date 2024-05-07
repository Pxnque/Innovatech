import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("e-StockTag Admin Panel")
        self.geometry("838x470")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure((1, 2,3,4,5), weight=0)
       

        # Create sidebar frame with widgets. FRAME LEFT BOX
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="e-StockTag", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=40, pady=(20, 10))

        # Button to display the 'Agregar Trabajador' frame
        self.sidebar_button = ctk.CTkButton(self.sidebar_frame, text="Registrar empleado", command=self.mostrar_agregar_trabajador)
        self.sidebar_button.grid(row=1, column=0, padx=40, pady=10)

        # Button to display the 'Ver Trabajadores' frame
        self.sidebar_button1 = ctk.CTkButton(self.sidebar_frame, text="Ver empleados", command=self.mostrar_ver_trabajadores)
        self.sidebar_button1.grid(row=2, column=0, padx=40, pady=10)

        

        # Main content area. FRAME RIGHT BOX.
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, rowspan=7, sticky="nsew")

        # Frame for 'Agregar Trabajador'
        self.agregar_trabajador_frame = ctk.CTkFrame(self.main_frame)
        self.agregar_trabajador_frame.grid(row=0, column=0, sticky="nsew")
        self.agregar_trabajador_frame.grid_remove()  # Hide initially

        self.label_1 = ctk.CTkLabel(self.agregar_trabajador_frame, text="Ingresar datos del trabajador",font=ctk.CTkFont(size=20,weight="bold"))
        self.label_1.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.entry = ctk.CTkEntry(self.agregar_trabajador_frame, placeholder_text="Nombre",width=350)
        self.entry.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.string_input_button_2 = ctk.CTkEntry(self.agregar_trabajador_frame, placeholder_text="Apellido Materno",width=350)
        self.string_input_button_2.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        self.string_input_button_3 = ctk.CTkEntry(self.agregar_trabajador_frame, placeholder_text="Apellido Paterno",width=350)
        self.string_input_button_3.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.string_input_button_4 = ctk.CTkEntry(self.agregar_trabajador_frame, placeholder_text="Linea de trabajo",width=350)
        self.string_input_button_4.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        
        self.main_button_1 = ctk.CTkButton(master=self.agregar_trabajador_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Agregar trabajador",command=self.sidebar_button_event)
        self.main_button_1.grid(row=5, column=0, padx=(20, 20), pady=70, sticky="w")

        # Frame for 'Ver Trabajadores'
        self.ver_trabajadores_frame = ctk.CTkFrame(self.main_frame)
        self.ver_trabajadores_frame.grid(row=0, column=0, sticky="nsew")
        self.ver_trabajadores_frame.grid_remove()  # Hide initially

        self.tabla = ttk.Treeview(self.ver_trabajadores_frame, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.ver_trabajadores_frame, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.ver_trabajadores_frame, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Nombre', 'Apellido Materno', 'Apellido Paterno', 'Linea')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla.column('Apellido Materno', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Apellido Paterno', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Linea', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Id', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Apellido Materno', text='Apellido Materno', anchor ='center')
        self.tabla.heading('Apellido Paterno', text='Apellido Paterno', anchor ='center')
        self.tabla.heading('Linea', text='Linea', anchor ='center')

        estilo = ttk.Style(self.ver_trabajadores_frame)
        estilo.theme_use('alt') 
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        
    def mostrar_agregar_trabajador(self):
        self.ver_trabajadores_frame.grid_remove()
        self.agregar_trabajador_frame.grid()

    def mostrar_ver_trabajadores(self):
        self.agregar_trabajador_frame.grid_remove()
        self.ver_trabajadores_frame.grid()
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            sql = "SELECT * FROM trabajador " 
            cursor.execute(sql)
            registro = cursor.fetchall()
            i = -1
            for i in range(len(registro)):  # Iterar sobre un rango de 0 a la longitud de los registros - 1
                self.tabla.insert('', i, text=registro[i][0], values=registro[i][1:])
        except Exception as e:
            messagebox.showerror("Error",e)

    
    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
 
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
            self.entry.set('')
            self.string_input_button_2.set('')
            self.string_input_button_3.set('')
            self.string_input_button_4.set('')
        except Exception as e:
            messagebox.showerror("Error",e)

if __name__ == "__main__":
    app = App()
    app.mainloop()
