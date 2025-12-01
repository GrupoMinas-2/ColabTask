from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from app.interface.widgets.modalTask_iten import ModalTask
from app.interface.widgets.task_iten import Task
from app.domain.useCases.create_task import useCase_createTask

Builder.load_file('dev/app/interface/kvLang/TasksPage.kv')

class TasksPage(Screen):
    def open_TaskPage(self, idnucleo):
        self.currentNucleo = idnucleo
        print("acessou o nucleo")
        


    def insertModal(self):
        self.modal= ModalTask()
        self.modal.parent_screen = self
        self.modal.open()
        
    def insertTask(self):
        self.use_case= useCase_createTask()

        titulo= self.modal.ids.inputTitle.text
        prazo= self.modal.ids.inputDate.text
        responsavel= self.modal.ids.inputPerson.text
        descricao=self.modal.ids.inputDescription.text

        result = self.use_case.executeCreateTask(titulo, prazo, responsavel, descricao, self.currentNucleo)

        if result["sucess"]: 
            self.ids.containerTasks.add_widget(
                Task(titulo, prazo, responsavel, descricao) # reordenar
            )
            print(result["message"])
        
        else:
            print("Tarefa não foi criada!")
    