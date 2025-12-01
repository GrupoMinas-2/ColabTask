from app.data.repositories.task_repository import Task_repository
from app.domain.entities.task import Task

class Task_service:
    def __init__(self):
        self.repository = Task_repository()


    def create(self, titleTask, descriptionTask, statusTask, end_dateTask, idnucleoTask):

        if not titleTask.strip():
            titleTask = "Tarefa"
        if not statusTask.strip():
            statusTask = "não iniciado"

        newTask= Task(titleTask, descriptionTask, statusTask, end_dateTask, idnucleoTask)
        register= self.repository.insert_register(newTask)

        return{
            "sucess": True,
            "message": "tarefa criada!",
            "id": register[0]
        }
