import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import socket
import sqlite3

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("CustomTkinter Complex Example")
        self.geometry("768x540")

        
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure((1, 2,3,4,5), weight=0)

        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")

        # Logo label
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Nombre empresa", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=40, pady=(20, 10))

        # Sidebar button
        self.sidebar_button = ctk.CTkButton(self.sidebar_frame, text="Registrar empleado")
        self.sidebar_button.grid(row=1, column=0, padx=40, pady=10)

        # Main content area
        # Column 1
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
        

        # Column 2
        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text="Agregar trabajador",command=self.sidebar_button_event)
        self.main_button_1.grid(row=5, column=1, padx=(20, 20), pady=70, sticky="w")

        
        
        

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
    


 