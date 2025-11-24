from app.data.database import Database
from app.data.repositories.user_nucleo_repository import User_Nucleo_repository

class Nucleo_repository:
    def __init__(self):
        self.database= Database()
        self.conectrepository = User_Nucleo_repository()

    def insert_nucleo(self, nucleo):

        query = """
            INSERT INTO nucleos (title_nucleo, decription) VALUES (?, ?)
        """
        parms= (nucleo.title, 
                nucleo.description)
        
        self.database.setData_one(query, parms)

        nucleoId = self.find_by_name(nucleo.title)
        userId = self.database.session.user_id
        self.conectrepository.conet_user_nucleo(userId,nucleoId)



    def find_by_name(self, title):
        query = """
            SELECT * FROM nucleos WHERE title_nucleo = ?
        """
        parms = (title,)

        result= self.database.readData_one(query, parms)
        
        idnucleo= self.database.session.current_nucleoId= result[0]

        return idnucleo
    
    