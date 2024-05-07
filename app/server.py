import sqlite3
import hashlib
import socket
import threading

class conexion_BD():
    def __init__(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #si queremos que multiples equipos se conecten al servidor dejamos en blando el localhost
        server.bind(("localhost",9999))
        #Podemos poner un limite a las conexiones si pones un numero adentro del listen
        server.listen()

        def handle_connection(c):
            c.send("Username: ".encode())
            username = c.recv(1024).decode()
            c.send("Password: ".encode())
            password = c.recv(1024)
            password = hashlib.sha256(password).hexdigest()

            conn = sqlite3.connect("database.db")
            cur = conn.cursor()

            cur.execute("SELECT * FROM admins WHERE username = ? AND password = ?",(username,password))

            if cur.fetchall():
                c.send("1".encode())
            else:
                c.send("Usuario o contraseña incorrectos".encode())

        def insertar_trabajadores(nombre,apellidoM,apellidoP,linea):
            try:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                sql='''INSERT INTO trabajador (nombre, apellidoM, apellidoP, linea) 
                VALUES('{}', '{}','{}','{}')'''.format(nombre, apellidoM, apellidoP, linea)
                cursor.execute(sql)
                conn.commit()
                conn.close()
                
            except Exception as e:
                return

        while True:
            client, addr = server.accept()
            threading.Thread(target=handle_connection,args=(client,)).start()



    
