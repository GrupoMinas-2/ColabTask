from app.domain.services.authentication import Auth_service

class useCase_registerUser:
    def __init__(self):
        self.serviceAuth= Auth_service()
    
    def executeRegister(self, email, name, pasword):
        
        result= self.serviceAuth.register(email=email, name= name, pasword= pasword)

        if not result["sucess"]:
            return result

        return {"sucess": True, "message": "Usuário criado"}
    