from datetime import datetime
from src.models.task import Task
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, description: str) -> Task:
        """Add task"""
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        description = description.strip()
        task_id = self.repository.get_next_id()
        task = Task(task_id, description)
        self.repository.save_task(task)
        return task

    def update_task(self, task_id: int, new_description: str) -> Task:
        """Update task description"""
        if not new_description or not new_description.strip():
            raise ValueError("Description cannot be empty")

        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found")

        task.description = new_description.strip()
        self.repository.update_task(task)
        return task
