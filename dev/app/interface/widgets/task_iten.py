from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('dev/app/interface/kvLang/Task.kv')

class Task(BoxLayout):
    def __init__( self, title= ' ', date= ' ', person= ' ', description = '', **kwargs): 

        super().__init__(**kwargs)
        self.ids.taskTitle.text= title
        self.ids.taskDescription.text= date
        self.ids.tasDate.text= person
        self.ids.taskPerson.text= description