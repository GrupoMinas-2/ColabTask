from app.data.database import Database

class User_Nucleo_repository:
    def __init__(self):
        self.database= Database()
    
    def conect_user_nucleo (self, iduser, idnucleo):
        query= """
            INSERT INTO user_nucleo(user_id, nucleo_id)
            VALUES (?,?) 
        """
        parms = (iduser, idnucleo)

        self.database.setData_one(query, parms)