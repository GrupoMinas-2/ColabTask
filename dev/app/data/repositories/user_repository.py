from app.data.database import Database 

class Usee_repository:
    def __init__(self):
        self.dataBase = Database()
        self.email= None
        

    def insert_register(self, user):
        query= """ 
            INSERT INTO users (email, name, password)
            VALUES (?,?,?) RETURNING *
        """

        parms =(user.email,
                user.name, 
                user.pasword)

        result = self.dataBase.setData_one(query , parms)

        return result
    

    def find_by_email(self, email ):
        query= " SELECT * FROM users WHERE email = ? "
        value= (email, )
        result= self.dataBase.readData_one(query, value)
        if not result is None:
            self.email =result[1]

        return result
    

    def find_nucleo_user(self, iduser):

        query= """
            SELECT * FROM nucleos AS n 
            INNER JOIN user_nucleo un
            ON n.idnucleo = un.nucleo_id
            WHERE un.user_id = ? 
        """

        value= (iduser,)

        result= self.dataBase.readData_all(query, value)

        return result
        
