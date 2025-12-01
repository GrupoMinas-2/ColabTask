from app.data.database import Database

class Task_repository:
    def __init__(self):
        self.dataBase = Database()
    


    def insert_register(self, task):
        
        query = """ 
            INSERT INTO tasks (title_task, end_date, status, description, nucleo_id) 
            VALUES(?,?,?,?,?)
            RETURNING *
        """
        value = (task.title, task.end_date, task.status, task.description, task.nucleo_id)

        result = self.dataBase.setData_one(query, value)

        print(result[0])

        return result
    


    def find_Tasks_by_nucleo(self, idnucleo):

        query= """
            SELECT * FROM tasks WHERE nucleo_id = ?
        """
        value = (idnucleo, )
        
        result = self.dataBase.readData_all(query, value)

        print(result)
        
        return result