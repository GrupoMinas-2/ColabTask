from app.data.repositories.nucleo_repository import Nucleo_repository
from app.domain.entities.nucleo import Nucleo
from app.data.repositories.user_repository import Usee_repository

class Nucleo_service:
    def __init__(self):
        self.repository= Nucleo_repository()
        self.userRepository= Usee_repository()
    
    
    def create(self, title, description):
        
        newNucleo = Nucleo(title, description)
        self.repository.insert_nucleo(newNucleo)
        return{
            "sucess": True,
            "message": "núcleo criado!"
        }
    
    
    def getId_Nucleo(self, title):
        dataNucleo= self.repository.find_by_name(title)
        return dataNucleo[0]
    

    def get_Nucleos(self, email):
        return self.userRepository.find_nucleo_user(email)
