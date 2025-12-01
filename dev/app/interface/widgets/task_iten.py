from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('dev/app/interface/kvLang/task.kv')

class Task(BoxLayout):
    def __init__( self, title= "tarefa", date= "12", person= "eu mesmo", description = "ir no mercado", **kwargs): 
        if not title.strip():
            self.title = "Tarefa"
        else:
            self.title = title

        if not date.strip():
            self.date = "dd/mm/aaaa"
        else:
            self.date = date

        if not person.strip():
            self.person= "eu mesmo"
        else:
            self.person = person

        if not description.strip():
            self.description= "vazio"
        else:
            self.description = description
        

        super().__init__(**kwargs)
        self.ids.taskTitle.text= self.title
        self.ids.taskDate.text= self.date
        self.ids.taskPerson.text= self.person
        self.ids.taskDescription.text= self.description