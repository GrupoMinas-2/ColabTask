from app.data.database import Database 

class Usee_repository:
    def __init__(self):
        self.dataBase = Database()

    def insert_register(self, user):
        query= """ 
            INSERT INTO users (email, name, password)
            VALUES (?,?,?)
        """

        parms =(user.email,
                user.name, 
                user.password)

        self.dataBase.setData_one(query , parms)
    

    def find_by_email(self, email ):
        query= " SELECT * FROM users WHERE email = ? "
        value= (email, )
        result= self.dataBase.readData_one(query, values= value)
        return result
        
