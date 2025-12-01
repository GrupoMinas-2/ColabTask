from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('dev/app/interface/kvLang/task_page.kv')

class Task_screen(Screen):
    def open_Task(self, task):
        self.ids.nametask.text= task.title
        self.ids.dateTask.text= task.date
        self.ids.personTask.text= task.person
        self.ids.descriptionTask.text= task.description
        pass
