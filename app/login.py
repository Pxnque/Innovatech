import tkinter
from tkinter import messagebox
from tkinter import *
import socket
from empleados import App



#window creation
window = tkinter.Tk()
window.title("Login")
window.geometry('838x470')
window.configure(bg='#DBDBDB')

def launch_empleados_app():
    app = App()  # Create an instance of the App class from empleados.py
    app.mainloop()

def login():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",9999))

    message = client.recv(1024).decode()
    client.send(username_entry.get().encode())
    message = client.recv(1024).decode()
    client.send(password_entry.get().encode())
    msg = client.recv(1024).decode()
    if msg == "1":
        window.destroy()
        launch_empleados_app()
        
    else:
        messagebox.showinfo(title="Login failed",message=msg)
    
    

frame = tkinter.Frame(bg='#DBDBDB')


login_label = tkinter.Label(
    frame, text="Iniciar sesión", bg='#DBDBDB', fg="#056571", font=("System", 30))
username_label = tkinter.Label(
    frame, text="Usuario", bg='#DBDBDB', fg="#000000", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Contraseña", bg='#DBDBDB', fg="#000000", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#056571", fg="#FFFFFF", font=("Arial", 16), command=login)


login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, sticky='W')
username_entry.grid(row=2, column=0, pady=10)
password_label.grid(row=3, column=0, sticky='W',pady=[20,7])
password_entry.grid(row=4, column=0)
login_button.grid(row=5, column=0, columnspan=3, pady=30,sticky='WE')

frame.pack()

window.mainloop()