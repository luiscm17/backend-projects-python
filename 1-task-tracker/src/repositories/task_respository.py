from typing import List, Optional
from src.models.task import Task
from src.utils.file_handler import FileHandler


class TaskRepository:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def get_next_id(self) -> int:
        """Get next id"""
        tasks_data = self.file_handler.read_task()
        if not tasks_data:
            return 1
        return max(task["id"] for task in tasks_data) + 1

    def save_task(self, task: Task) -> None:
        """Save task"""
        tasks_data = self.file_handler.read_task()
        tasks_data.append(task.to_dict())
        self.file_handler.write_task(tasks_data)

    def find_by_id(self, task_id: int) -> Optional[Task]:
        """Find task by id"""
        tasks_data = self.file_handler.read_task()
        for task_data in tasks_data:
            if task_data["id"] == task_id:
                task = Task(
                    task_data["id"], task_data["description"], task_data["status"]
                )
                task.created_at = task_data["created_at"]
                task.updated_at = task_data["updated_at"]
                return task
        return None

    def find_all(self) -> List[Task]:
        """Get all tasks"""
        tasks_data = self.file_handler.read_task()
        tasks = []
        for task_data in tasks_data:
            task = Task(task_data["id"], task_data["description"], task_data["status"])
            task.created_at = task_data["created_at"]
            task.updated_at = task_data["updated_at"]
            tasks.append(task)
        return tasks

    def find_by_status(self, status: str) -> List[Task]:
        """Get task by status"""
        tasks_data = self.file_handler.read_task()
        tasks = []
        for task_data in tasks_data:
            if task_data["status"] == status:
                task = Task(
                    task_data["id"], task_data["description"], task_data["status"]
                )
                task.created_at = task_data["created_at"]
                task.updated_at = task_data["updated_at"]
                tasks.append(task)
        return tasks

    def update_task(self, task: Task) -> None:
        """Update task"""
        tasks_data = self.file_handler.read_task()

        for i, task_data in enumerate(tasks_data):
            if task_data["id"] == task.id:
                tasks_data[i] = task.to_dict()
                break
        self.file_handler.write_task(tasks_data)

    def delete_task(self, task_id: int) -> bool:
        """Delete task by id"""
        tasks_data = self.file_handler.read_task()

        for i, task_data in enumerate(tasks_data):
            if task_data["id"] == task_id:
                del tasks_data[i]
                self.file_handler.write_task(tasks_data)
                return True
        return False
