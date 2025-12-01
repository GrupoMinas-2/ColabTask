from app.domain.services.task_service import Task_service

class useCase_createTask:
    def __init__(self):
     self.service= Task_service()

    def executeCreateTask(self, titleTask, descriptionTask, statusTask, end_dateTask, idnucleoTask):
       result = self.service.create(titleTask, descriptionTask, statusTask, end_dateTask, idnucleoTask)
       return result