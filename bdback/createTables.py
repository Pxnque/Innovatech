import sqlite3
import hashlib

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
)
            """)

username1,pass1 = "loaiza69",hashlib.sha256("tagstock777".encode()).hexdigest()
username2,pass2 = "emi",hashlib.sha256("2121".encode()).hexdigest()
cur.execute("INSERT INTO admins (username,password) VALUES (?,?)",(username1,pass1))
cur.execute("INSERT INTO admins (username,password) VALUES (?,?)",(username2,pass2))

conn.commit()