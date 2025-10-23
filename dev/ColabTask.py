
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
    # def __init__( self, titulo, descrição, imagem, **Kwargs ):
    #    super().__init__(**Kwargs)
    def insertModal(self):
        
        modal= ModalNucleo()
        modal.parent_screen = self
        modal.open()


class ModalNucleo(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass


class ColabTask(App): 
    def build(self):
        return ControllerTelas()


ColabTask().run()