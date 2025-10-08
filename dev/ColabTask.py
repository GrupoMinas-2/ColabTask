from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')

class ControllerTelas(ScreenManager):
    pass

class LoginPage(Screen):
    pass

class ColabTask(App): 
    def build(self):
        return ControllerTelas()


ColabTask().run()