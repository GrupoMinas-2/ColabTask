from app.data.database import Database
from app.data.repositories.user_nucleo_repository import User_Nucleo_repository

class Nucleo_repository:
    id_nucleo = None

    def __init__(self):
        self.database= Database()
        self.conectrepository = User_Nucleo_repository()

    def insert_nucleo(self, nucleo):

        query = """
            INSERT INTO nucleos (title_nucleo, decription) VALUES (?, ?)
            RETURNING *
        """
        parms= (nucleo.title, 
                nucleo.description)
        
        result = self.database.setData_one(query, parms)

        self.id_nucleo = result[0]
        print (self.id_nucleo)
        
        return result


    #def find_by_name(self, title):
    #    query = """
    #        SELECT * FROM nucleos WHERE title_nucleo = ?
    #    """
    #    parms = (title,)
#
    #    result= self.database.readData_one(query, parms)
    #    
    #    idnucleo= self.database.session.current_nucleoId= result[0]
#
    #    return idnucleo
    
    