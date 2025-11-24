from app.data.database import Database 

class Usee_repository:
    def __init__(self):
        self.dataBase = Database()
        self.email= None
        

    def insert_register(self, user):
        query= """ 
            INSERT INTO users (email, name, password)
            VALUES (?,?,?)
        """

        parms =(user.email,
                user.name, 
                user.pasword)

        self.dataBase.setData_one(query , parms)
    

    def find_by_email(self, email ):
        query= " SELECT * FROM users WHERE email = ? "
        value= (email, )
        result= self.dataBase.readData_one(query, value)
        
        self.email =result[1]

        self.dataBase.session.user_id= result[0] 

        return result
    

    def find_nucleo_user(self, email):
        iduser= self.find_by_email(email)

        query= """
            SELECT * FROM nucleos AS n 
            INNER JOIN user_nucleo un
            ON n.idnucleo = un.user_id
            WHERE un.user_id = ? 
        """

        value= (iduser[0],)

        result= self.dataBase.readData_all(query, value)

        return result
        
