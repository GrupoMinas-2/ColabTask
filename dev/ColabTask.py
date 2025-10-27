
from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.factory import Factory
from kivy.uix.modalview import ModalView 


class ControllerTelas(ScreenManager):
    pass


class LoginPage(Screen):
    pass


class RegisterPage(Screen):
    pass


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

class ModalNucleo(ModalView):
    pass

class Nucleo(BoxLayout):
    def __init__( self, titulo='tarefa', descrição='desc',**Kwargs ): 
        if not titulo.strip():
            titulo = "nome núcleo"
        if not descrição.strip():
            descrição= "descrição"

        # atribuit valor a descrição
        super().__init__(**Kwargs)
        self.ids.nucleoTitle.text = titulo
        self.ids.taskDescription.text= descrição


class TasksPage(Screen):
    def insertModal(self):
        self.modal= ModalTask()
        self.modal.parent_screen = self
        self.modal.open()
        pass

class ModalTask(ModalView):
    pass


class ColabTask(App): 
    def build(self):
        return ControllerTelas()


ColabTask().run()