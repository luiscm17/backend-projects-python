from typing import List
from src.models.task import Task
from src.utils.file_handler import FileHandler


class TaskRepository:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def get_next_id(self) -> int:
        tasks_data = self.file_handler.read_task()
        if not tasks_data:
            return 1
        return max(task["id"] for task in tasks_data) + 1

    def save_task(self, task: Task) -> None:
        tasks_data = self.file_handler.read_task()
        tasks_data.append(task.to_dict())
        self.file_handler.write_task(tasks_data)
