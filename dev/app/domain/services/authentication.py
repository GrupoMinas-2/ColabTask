from app.data.repositories.user_repository import Usee_repository
from app.domain.entities.user import User

class Auth_service: 
    def __init__(self):
        self.repository= Usee_repository()

    def register(self, email, name, pasword):
        
        if self.repository.find_by_email(email): 
            return {
                "sucess": False,
                "response": "usuário já existe"
            }
        
        newUser= User(self, email= email, name= name, pasword= pasword)

        self.repository.insert_register(newUser)
        return {
                "sucess": True,
                "response": "usuário cadastrado"
            }
