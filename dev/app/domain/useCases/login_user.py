from app.domain.services.authentication import Auth_service
from app.domain.services.session import Session

class usecase_login:
    def __init__(self):
        self.service = Auth_service()

    def executeLogin(self, email, pasword):
        result = self.service.login_acaunt(email, pasword)

        if not result["sucess"]:
            return result
        
        else:
            self.session = Session()
            self.session.user_id = result["iduser"]
            return {"sucess": True, "message": "Login bem sucedido!"}