from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('dev/app/interface/kvLang/task.kv')

class Task(BoxLayout):
    def __init__( self, title= "tarefa", date= "12", person= "eu mesmo", description = "ir no mercado", **kwargs): 
        if not title.strip():
            title = "Tarefa"
        if not date.strip():
            date = "dd/mm/aaaa"
        if not person.strip():
            person= "eu mesmo"
        if not description.strip():
            description= "vazio"


        super().__init__(**kwargs)
        self.ids.taskTitle.text= title
        self.ids.taskDate.text= date
        self.ids.taskPerson.text= person
        self.ids.taskDescription.text= description