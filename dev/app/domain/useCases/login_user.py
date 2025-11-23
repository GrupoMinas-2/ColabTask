from app.domain.services.authentication import Auth_service

class usecase_login:
    def __init__(self):
        self.service = Auth_service()

    def executeLogin(self, email, pasword):
        result = self.service.login_acaunt(email, pasword)

        if not result["sucess"]:
            return result
        else:
            return {"sucess": True, "message": "Login bem sucedido!"}