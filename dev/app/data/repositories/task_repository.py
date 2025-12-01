from app.data.database import Database

class Task_repository:
    def __init__(self):
        self.dataBase = Database()
    
    def insert_register(self, task):
        
        query = """ 
            INSERT INTO tasks (title_task, description, status, end_date, nucleo_id) 
            VALUES(?,?,?,?,?)
            RETURNING *
        """
        parms = (task.title, task.description, task.status, task.end_date, task.nucleo_id)

        result = self.dataBase.setData_one(query, parms)

        print(result[0])

        return result
        