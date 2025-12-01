from app.data.repositories.user_repository import Usee_repository
from app.data.repositories.nucleo_repository import Nucleo_repository
from app.domain.entities.nucleo import Nucleo

class Nucleo_service:
    def __init__(self):
        self.repository= Nucleo_repository()
        self.userRepository= Usee_repository()
    
    
    def create(self, title, description):
        
        if not title.strip():
            title = "Nome núcleo"
        if not description.strip():
            description= "sem descrição"

        newNucleo = Nucleo(title, description)
        register = self.repository.insert_nucleo(newNucleo)
        return{
            "sucess": True,
            "message": "núcleo criado!",
            "id": register[0]
        }
    
    
    def getNucleo_byID(self, idnucleo):
        dataNucleo= self.repository.find_by_id(idnucleo)
        return dataNucleo
    

    def get_Nucleos(self, iduser):
        return self.userRepository.find_nucleo_user(iduser)
