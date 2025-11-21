from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from app.interface.widgets.nucleo_iten import Nucleo
from app.interface.widgets.modalNucleo_iten import ModalNucleo

Builder.load_file('dev/app/interface/kvLang/HomePage.kv')

class HomePage(Screen):

    def insertModal(self):
        self.modal= ModalNucleo()
        self.modal.parent_screen = self
        self.modal.open()

    def insertNucleo(self):
        self.modal.parent_screen = self
        titulo= self.modal.ids.inputTitle.text
        descricao=self.modal.ids.inputDescription.text

        self.ids.containerNucleos.add_widget(
            Nucleo(titulo, descricao)
        ) 