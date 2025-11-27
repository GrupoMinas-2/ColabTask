from app.domain.services.session import Session
from app.data.repositories.user_repository import Usee_repository
from app.domain.entities.user import User

class Auth_service: 
    def __init__(self):
        self.repository= Usee_repository()
        self.session = Session()
            

    def register(self, email, name, pasword):        

        if self.repository.find_by_email(email): 
            return {
                "sucess": False,
                "response": "Usuário já existente! \nUse outro email para o cadastro."
            }
        
        if (not email.strip()) or (not name.strip()) or (not pasword.strip()):
            return {
                "sucess": False,
                "response": "Preencha todods os campos para realizar o cadastro com sucesso"
            }
        
        if not self.repository.find_by_email(email): 
            newUser= User(email, name, pasword)

            self.repository.insert_register(newUser)
            return {
                "sucess": True,
                "response": "usuário cadastrado"
            }
        
        
    def login_acaunt(self, email, pasword):
        
        dataUser= self.repository.find_by_email(email)
        
        if dataUser:
            
            if  dataUser[3] == pasword: 

                self.session.user_id = dataUser[0]

                return {
                    "sucess": True,
                    "message": "Senha correta!",
                    "iduser": dataUser[0]
                }
            else: 
                return {
                    "sucess": False,
                    "message": "Senha incorreta!"
                }
        else: 
            return {
                    "sucess": False,
                    "message": "Usuário não encontrado!"
                }

            