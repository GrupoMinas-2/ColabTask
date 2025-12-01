from app.data.repositories.task_repository import Task_repository
from app.domain.entities.task import Task

class Task_service:
    def __init__(self):
        self.repository = Task_repository()


    def create(self, titleTask, end_dateTask, statusTask, descriptionTask= "sem descrição", idnucleoTask= 0):

        if not titleTask.strip():
            titleTask = "Tarefa"
        
        if statusTask is None:
            statusTask = "não iniciado"
            
        if idnucleoTask == 0:         
            return{
            "sucess": False,
            "message": "não é possível criar uma tarefa sem id do nucleo",
            "id": register[0]
            }

        newTask= Task(titleTask, end_dateTask, statusTask, descriptionTask, idnucleoTask)
        register= self.repository.insert_register(newTask)

        return{
            "sucess": True,
            "message": "tarefa criada!",
            "id": register[0]
        }
    
    

    def get_Tasks(self, idnucleo ):
        return self.repository.find_Tasks_by_nucleo(idnucleo)
    