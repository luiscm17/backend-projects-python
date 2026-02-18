from src.models.task import Task
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, description: str) -> Task:
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        description = description.strip()
        task_id = self.repository.get_next_id()
        task = Task(task_id, description)
        self.repository.save_task(task)
        return task
