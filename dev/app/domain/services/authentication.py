from app.data.repositories.user_repository import Usee_repository
from app.domain.entities.user import User

class Auth_service: 
    def __init__(self):
        self.repository= Usee_repository()

    def register(self, email, name, pasword):
        
        if self.repository.find_by_email(email): 
            return {
                "sucess": False,
                "response": "Usuário já existente! \nUse outro email para o cadastro."
            }
        else: 
            newUser= User(email, name, pasword)

            self.repository.insert_register(newUser)
            return {
                    "sucess": True,
                    "response": "usuário cadastrado"
                }
