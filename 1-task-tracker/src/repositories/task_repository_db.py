from typing import List, Optional
from src.models.task import Task
from src.utils.db_handler import DBHandler


class TaskRepositoryDB:
    def __init__(self, db_handler: DBHandler):
        self.db_handler = db_handler

    def get_next_id(self) -> int:
        """
        Get the next available task ID

        Returns:
            Next task ID
        """
        tasks = self.db_handler.get_all_tasks()
        if not tasks:
            return 1
        return max(task["id"] for task in tasks) + 1

    def save_task(self, task: Task) -> None:
        """
        Save a task

        Args:
            task: Task to save
        """
        self.db_handler.save_task(task)

    def find_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find task by ID

        Args:
            task_id: Task ID to find

        Returns:
            Task with the given ID or None if not found
        """
        tasks = self.db_handler.get_all_tasks()
        for task_data in tasks:
            if task_data["id"] == task_id:
                task = Task(
                    task_data["id"], task_data["description"], task_data["status"]
                )
                task.created_at = task_data["created_at"]
                task.updated_at = task_data["updated_at"]
                return task
        return None

    def find_all(self) -> List[Task]:
        """
        Find all tasks

        Returns:
            List of all tasks
        """
        tasks_data = self.db_handler.get_all_tasks()
        tasks = []
        for task_data in tasks_data:
            task = Task(task_data["id"], task_data["description"], task_data["status"])
            task.created_at = task_data["created_at"]
            task.updated_at = task_data["updated_at"]
            tasks.append(task)
        return tasks

    def find_by_status(self, status: str) -> List[Task]:
        """
        Find tasks by status

        Args:
            status: Task status to find

        Returns:
            List of tasks with the given status
        """
        tasks_data = self.db_handler.get_all_tasks()
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
        """
        Update a task
        """
        self.db_handler.update_task(task)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task
        """
        return self.db_handler.delete_task(task_id)
