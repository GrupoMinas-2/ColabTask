from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from app.interface.widgets.modalTask_iten import ModalTask
from app.interface.widgets.task_iten import Task
from app.domain.useCases.create_task import useCase_createTask
from app.domain.useCases.search_tasks import useCase_searchTasks
from app.domain.services.nucleo_service import Nucleo_service

Builder.load_file('dev/app/interface/kvLang/TasksPage.kv')

class TasksPage(Screen):
    def open_TaskPage(self, idnucleo):
        self.serviceNucleo= Nucleo_service()
        dataNucleo = self.serviceNucleo.getNucleo_byID(idnucleo)
        self.ids.nucleoTitle.text= dataNucleo[1]
        self.ids.nucleoDescription.text= dataNucleo[2]
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
        status = None

        result = self.use_case.executeCreateTask(titulo, prazo, status, descricao, self.currentNucleo)

        if result["sucess"]: 
            self.ids.containerTasks.add_widget(
                Task(titulo, prazo, responsavel, descricao) # reordenar
            )
            print(result["message"])
        
        else:
            print("Erro ao criar tarefa: ", result["message"] )
    
    def searchTasks_byNucleo(self):
        self.use_case= useCase_searchTasks()
        listTasks= self.use_case.executeSearchTask(self.currentNucleo)

        for task in listTasks:
            self.ids.containerTasks.add_widget(
                Task(task[1], task[2], task[3], task[4])
            )
        