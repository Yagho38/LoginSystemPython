import sqlite3

#Conexao
conn = sqlite3.connect('UserData.db')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Connected to Database")