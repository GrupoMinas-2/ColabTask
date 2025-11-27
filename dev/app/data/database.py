#from kivy.uix.filechooser import error
#import os
import sqlite3
from app.domain.services.session import Session


class Database:
    session = Session()

    def __init__(self):
        self.connection = sqlite3.connect('dev/app/data/colabtask.db')
        self.cursor = self.connection.cursor()

        # Tabela de usuários --- 
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


        # Tabela de nucleos --- 
        try: 
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS nucleos(
                    idnucleo INTEGER PRIMARY KEY AUTOINCREMENT,
                    title_nucleo TEXT NOT NULL, 
                    decription TEXT
                )
            """)
        except sqlite3.Error as erro:
            print("Erro ao criar tabela:", erro)


        # Tabela de tarefas --- 
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks(
                    idtask INTEGER PRIMARY KEY AUTOINCREMENT,
                    title_task TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    end_date TEXT, 
                    nucleo_id INTEGER NOT NULL,
                    FOREIGN KEY (nucleo_id) REFERENCES nucleo(id)
                )
            """)
        except sqlite3.Error as erro:
            print("Erro ao criar tabela: ", erro)


        # tabela de relação usuário <--> núcleo 
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_nucleo(
                    user_id INTEGER NOT NULL,
                    nucleo_id INTEGER NOT NULL,
                    PRIMARY KEY (user_id, nucleo_id),
                    FOREIGN KEY (user_id) REFERENCES users(iduser),
                    FOREIGN KEY (nucleo_id) REFERENCES nucleos(idnucleo)
                )
            """)
        except sqlite3.Error as erro:
            print("Erro ao criar tabela: ", erro)


        # tabela de relação usuário <--> task
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_task(
                    user_id INTEGER NOT NULL, 
                    task_id INTEGER NOT NULL,
                    PRIMARY KEY (user_id, task_id),
                    FOREIGN KEY (user_id) REFERENCES users(iduser),
                    FOREIGN KEY (task_id) REFERENCES tasks(idtask)
                )
            """)
        except sqlite3.Error as erro: 
            print("Erro ao criar tabela: ", erro)

        self.connection.commit()


    # metódos de leitura e alteração
    def setData_one(self, query, values=()):
        self.cursor.execute(query , values)
        self.connection.commit()
        return self.cursor.fetchone()

    def readData_one(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def setData_all(self, query, values=()):
        self.cursor.executemany(query, values)
        self.connection.commit()
        return self.cursor.fetchall()

    def readData_all(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()


db= Database()
element = ("teste_Returning9","teste")

db.cursor.executemany("INSERT INTO nucleos (title_nucleo, decription) VALUES (?, ?) RETURNING *", (element,) )
print(db.cursor.fetchone())

idnuc = db.cursor.lastrowid
db.connection.commit()

db.cursor.execute("SELECT * FROM nucleos WHERE idnucleo =?", (idnuc,))
print(db.cursor.fetchone())


#b.cursor.execute("DROP TABLE nucleos")
#b.connection.commit()

#db.cursor.execute("""
#    CREATE TABLE IF NOT EXISTS nucleos_temp(
#        idnucleo INTEGER PRIMARY KEY AUTOINCREMENT,
#        title_nucleo TEXT NOT NULL UNIQUE, 
#        decription TEXT
#    )
#""")

#db.cursor.execute("""
#CREATE TABLE IF NOT EXISTS tasks_temp(
#    idtask INTEGER PRIMARY KEY AUTOINCREMENT,
#    title_task TEXT NOT NULL,
#    description TEXT,
#    status TEXT NOT NULL,
#    end_date TEXT, 
#    nucleo_id INTEGER NOT NULL,
#    FOREIGN KEY (nucleo_id) REFERENCES nucleo(idnucleo)
#)
#""")

#db.connection.commit()

#db.cursor.execute("DROP TABLE nucleos")
#db.cursor.execute("DROP TABLE tasks")
#db.cursor.execute("ALTER TABLE nucleos_temp RENAME TO nucleos")
#db.cursor.execute("ALTER TABLE tasks_temp RENAME TO tasks")
#db.connection.commit()