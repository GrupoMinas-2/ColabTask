from app.domain.services.task_service import Task_service

class useCase_createTask:
    def __init__(self):
     self.service= Task_service()

    def executeCreateTask(self, titleTask, end_dateTask, statusTask, descriptionTask, idnucleoTask):
       result = self.service.create(titleTask, end_dateTask, statusTask, descriptionTask, idnucleoTask)
       return result