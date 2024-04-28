import tkinter as tk
from tkinter import messagebox
import socket
import importlib.util
import os


class Login:
    def __init__(self,window):
        super().__init__()

        # Window configuration
        self.window = window
        self.window.title("Login")
        self.window.geometry('1280x720')
        self.window.configure(bg='#C4C4C4')

        # Create frame for login elements
        self.frame = tk.Frame(self, bg='#C4C4C4')

        # Creating widgets
        self.login_label = tk.Label(
            self.frame, text="Login", bg='#C4C4C4', fg="#FF3399", font=("Arial", 30))
        self.username_label = tk.Label(
            self.frame, text="Username", bg='#C4C4C4', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.password_label = tk.Label(
            self.frame, text="Password", bg='#C4C4C4', fg="#FFFFFF", font=("Arial", 16))
        self.password_entry = tk.Entry(self.frame, show="*", font=("Arial", 16))
        self.login_button = tk.Button(
            self.frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.login)

        # Placing widgets on the screen
        self.login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=30)

        # Pack frame to display it
        self.frame.pack()

    def login(self):
        # Establish socket connection with server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 9999))

        # Receive initial message from server
        message = client.recv(1024).decode()

        # Send username to server
        client.send(self.username_entry.get().encode())
        message = client.recv(1024).decode()

        # Send password to server
        client.send(self.password_entry.get().encode())

        # Receive login result from server
        msg = client.recv(1024).decode()

        # Close socket connection
        client.close()

        # Check login result and show appropriate message box
        if msg == "1":
            messagebox.showinfo(title="Login", message=msg)
            # If login successful, open employee page
            self.open_employee_page()
        else:
            messagebox.showinfo(title="Login failed", message=msg)

    def open_employee_page(self):
        # Get the path to the empleados.py file in the 'app' folder
        app_folder = os.path.join(os.path.dirname(__file__), 'app')
        empleados_path = os.path.join(app_folder, 'empleados.py')

        # Dynamically import the empleados module
        spec = importlib.util.spec_from_file_location("empleados", app_folder)
        empleados = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(empleados)

        # Create new window for employee page
        win = tk.Toplevel(self)
        empleados.App(win)
        self.withdraw()  # Hide the login window
        win.deiconify()  # Show the employee page window
    
def page():
    window = tk()
    Login(window)
    window.mainloop()

if __name__ == "__main__":
    page()
    
