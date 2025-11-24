from app.domain.services.nucleo_service import Nucleo_service

class useCase_createNucleo:
    def __init__(self):
        self.service= Nucleo_service()

    def executeCreation(self, title, description):
        result = self.service.create(title, description)
        return result 
    