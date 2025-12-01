from app.domain.services.task_service import Task_service

class useCase_searchTasks:
    def __init__(self):
        self.service= Task_service()

    def executeSearchTask(self, idnucleo):
        return self.service.get_Tasks(idnucleo)