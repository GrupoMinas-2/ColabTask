import sqlite3


class Database:
    
    def __init__(self):
        self.connection = sqlite3.connect('dev/app/data/colabtask.db')
        self.cursor = self.connection.cursor()
        self.createTable_users()
        self.createTable_nucleos()
        self.createTable_tasks()
        self.createTable_userNucleo()
        self.createTable_userTask()


    # Tabela de usuários --- 
    def createTable_users(self):
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
    def createTable_nucleos(self):
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

        #self.connection.commit()


    # Tabela de tarefas --- 
    def createTable_tasks(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks(
                    idtask INTEGER PRIMARY KEY AUTOINCREMENT,
                    title_task TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    end_date TEXT, 
                    nucleo_id INTEGER NOT NULL,
                    FOREIGN KEY (nucleo_id) REFERENCES nucleo(idnucleo)
                )
            """)
        except sqlite3.Error as erro:
            print("Erro ao criar tabela: ", erro)

        #self.connection.commit()


    # tabela de relação usuário <--> núcleo 
    def createTable_userNucleo(self):
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

        #self.connection.commit()


    # tabela de relação usuário <--> task
    def createTable_userTask(self):
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

        #self.connection.commit()


    # metódos de leitura e alteração
    def setData_one(self, query, values=()):
        self.cursor.execute(query , values)
        registro = self.cursor.fetchone()
        self.connection.commit()
        return registro

    def readData_one(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def setData_all(self, query, values=()):
        self.cursor.executemany(query, values)
        registros= self.cursor.fetchall()
        self.connection.commit()
        return registros

    def readData_all(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()


db= Database()
#element = ("teste_Returning9","teste")
#
#db.cursor.executemany("INSERT INTO nucleos (title_nucleo, decription) VALUES (?, ?) RETURNING *", (element,) )
#print(db.cursor.fetchone())
#
#idnuc = db.cursor.lastrowid
#db.connection.commit()
#
#db.cursor.execute("SELECT * FROM nucleos WHERE idnucleo =?", (idnuc,))
#print(db.cursor.fetchone())


#db.cursor.execute("DROP TABLE nucleos")
#db.connection.commit()

#db.cursor.execute("""
#    CREATE TABLE IF NOT EXISTS nucleos_temp(
#        idnucleo INTEGER PRIMARY KEY AUTOINCREMENT,
#        title_nucleo TEXT NOT NULL, 
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

#db.cursor.execute("DELETE FROM nucleos")
#db.cursor.execute("DELETE FROM user_nucleo")
#db.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'nucleos'")
#db.cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'user_nucleo'")
#db.connection.commit()

#    mascara = (idnucleo, titulo, descricao, user_id, nucleo_id)
#    
#    teste= [(3, 'testeGabriel', 'gabriel nucleo', 3, 1),
#            (3, 'testeGabriel', 'gabriel nucleo', 3, 2),
#            (3, 'testeGabriel', 'gabriel nucleo', 3, 3),
#            (3, 'testeGabriel', 'gabriel nucleo', 3, 4),
#            (3, 'testeGabriel', 'gabriel nucleo', 3, 12)]
#        
#    teste2= [(1, 'testes', 'testes', 3, 1),
#             (2, 'testes', 'teste', 3, 2),
#             (3, 'testeGabriel', 'gabriel nucleo', 3, 3),
#             (4, 'testeGabriel', 'gabriel nucleo', 3, 4),
#             (12, 'familia teste', 'so teste', 3, 12)]