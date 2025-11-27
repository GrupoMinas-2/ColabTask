from app.data.repositories.user_repository import Usee_repository
from app.data.repositories.nucleo_repository import Nucleo_repository
from app.data.repositories.user_nucleo_repository import User_Nucleo_repository


class Session:
    user_id = None
    current_nucleoId = None
    current_taskId= None

    def __init__(self):
        
        conectUserNucleo= User_Nucleo_repository()
        conectUserNucleo.conect_user_nucleo(self.user_id , self.current_nucleoId)

        