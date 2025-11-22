import os
import sqlite3

#os.makedirs("dev/app/data", exist_ok=True)
sqlite3.connect('dev/app/data/colabtask.db')


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('dev/app/data/colabtask.db')
        self.cursor = self.connection.cursor()

        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    iduser INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    name TEXT,
                    password TEXT
                )
            """)
        except sqlite3.Error as erro:
            print("Erro ao criar tabela:", erro)

        self.connection.commit()

    def setData_one(self, query, values=()):
        self.cursor.execute(query , values)
        self.connection.commit()

    def readData_one(self, query, values=()):
        self.cursor.execute(query, values)
        self.connection.commit()

    def setData_many(self, query, values=()):
        self.cursor.executemany(query, values)
        self.connection.commit()

    def readData_many(self, query, values=()):
        self.cursor.executemany(query, values)
        self.connection.commit()


#db= Database()