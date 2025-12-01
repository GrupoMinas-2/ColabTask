from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from app.interface.widgets.nucleo_iten import Nucleo
from app.interface.widgets.modalNucleo_iten import ModalNucleo
from app.domain.services.nucleo_service import Nucleo_service
from app.domain.useCases.create_nucleo import useCase_createNucleo
from app.domain.services.session import Session

Builder.load_file('dev/app/interface/kvLang/HomePage.kv')

class HomePage(Screen):
    session = Session()


    def inicializate_Session(self, iduser):
        self.session.user_id = iduser
        


    def insertModal(self):
        self.modal= ModalNucleo()
        self.modal.parent_screen = self
        self.modal.open()



    def insertNucleo(self):
        self.use_case= useCase_createNucleo()

        titulo= self.modal.ids.inputTitle.text
        descricao=self.modal.ids.inputDescription.text

        result= self.use_case.executeCreation(titulo, descricao)

        if result["sucess"]:
            print(result["message"])
            self.session.current_nucleoId = result["id"]
            self.session.conect_UserNucleo()

            self.ids.containerNucleos.add_widget(
                Nucleo(titulo, descricao, self.session.current_nucleoId)
            ) 

        else:
            print("Nucleo não foi criado!")
            
        
    
    def searchNucleos_byUser(self, iduser):
        service = Nucleo_service()
        listNucleos= service.get_Nucleos(iduser)
        print(listNucleos)
        for nucleo in listNucleos:
            self.ids.containerNucleos.add_widget(
                Nucleo(nucleo[1], nucleo[2], nucleo[0]) )