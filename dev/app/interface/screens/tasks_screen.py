from kivy.lang.builder import Builder
from kivy.uix.settings import text_type
from kivy.uix.screenmanager import Screen
from app.interface.widgets.modalTask_iten import ModalTask
from app.interface.widgets.task_iten import Task

Builder.load_file('dev/app/interface/kvLang/TasksPage.kv')

class TasksPage(Screen):
    def insertModal(self):
        self.modal= ModalTask()
        self.modal.parent_screen = self
        self.modal.open()
        
    def insertTask(self):
        self.modal.parent_screen = self  # tirar
        titulo= self.modal.ids.inputTitle.text
        prazo= self.modal.ids.inputDate.text
        responsavel= self.modal.ids.inputPerson.text
        descricao=self.modal.ids.inputDescription.text

        self.ids.containerTasks.add_widget(
            Task(titulo, prazo, responsavel, descricao) # reordenar
        )

    