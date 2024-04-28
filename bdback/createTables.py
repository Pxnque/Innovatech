import sqlite3
import hashlib

conn = sqlite3.connect("database.db")
cur = conn.cursor()

#cur.execute(""" 
#CREATE TABLE IF NOT EXISTS admins (
#            id INTEGER PRIMARY KEY,
#            username VARCHAR(255) NOT NULL,
#            password VARCHAR(255) NOT NULL
#)
#            """)

cur.execute(""" 
CREATE TABLE IF NOT EXISTS trabajador (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            apellidoM VARCHAR(255) NOT NULL,
            apellidoP VARCHAR(255) NOT NULL,
            estado INTEGER NOT NULL DEFAULT 1 CHECK(estado IN (0, 1))

)
            """)

#username1,pass1 = "loaiza69",hashlib.sha256("tagstock777".encode()).hexdigest()
#username2,pass2 = "emi",hashlib.sha256("2121".encode()).hexdigest()
nombre1,apellidoM1,apellidoP1 = "Diego","Morales","Ramírez"
#cur.execute("INSERT INTO admins (username,password) VALUES (?,?)",(username1,pass1))
cur.execute("INSERT INTO trabajador (nombre,apellidoM,apellidoP) VALUES (?,?,?)",(nombre1,apellidoM1,apellidoP1))

conn.commit()