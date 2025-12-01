from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from app.interface.screens.login_screen import LoginPage
from app.interface.screens.register_screen import RegisterPage
from app.interface.screens.home_screen import HomePage
from app.interface.screens.tasks_screen import TasksPage
from app.interface.screens.task_screen import Task_screen

class Root(ScreenManager):
    pass

class ColabTask(App):
    def build(self):
        Builder.load_file("app/interface/kvLang/LoginPage.kv")
        Builder.load_file("app/interface/kvLang/RegisterPage.kv")
        Builder.load_file("app/interface/kvLang/HomePage.kv")
        Builder.load_file("app/interface/kvLang/TasksPage.kv")
        Builder.load_file("dev/app/interface/kvLang/task_page.kv")

        sm = Root()
        sm.add_widget(LoginPage())
        sm.add_widget(RegisterPage())
        sm.add_widget(HomePage())
        sm.add_widget(TasksPage())
        sm.add_widget(Task_screen())
        return sm

if __name__ == "__main__":
    ColabTask().run()