from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'width', '400')

class ControlerTelas(ScreenManager):
    pass

class LoginPage(Screen):
    pass

class ColabTask(App): 
    def build(self):
        return ControlerTelas()


ColabTask().run()