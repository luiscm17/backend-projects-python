from typing import List
from datetime import datetime
from src.models.task import Task
from src.repositories.task_repository_db import TaskRepositoryDB


class TaskService:
    def __init__(self, repository: TaskRepositoryDB):
        self.repository = repository

    def add_task(self, description: str) -> Task:
        """
        Add a new task

        Args:
            description: Task description

        Returns:
            Created task
        """
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        description = description.strip()
        task_id = self.repository.get_next_id()
        task = Task(task_id, description)
        self.repository.save_task(task)
        return task

    def list_all_tasks(self) -> List[Task]:
        """
        List all tasks

        Returns:
            List of all tasks
        """
        return self.repository.find_all()

    def list_tasks_by_status(self, status: str) -> List[Task]:
        """
        List tasks by status

        Args:
            status: Task status to filter

        Returns:
            List of tasks with the given status
        """
        if status not in ["all", "todo", "in-progress", "done"]:
            raise ValueError(
                "Invalid status: Use 'all', 'todo', 'in-progress' or 'done'"
            )

        if status == "all":
            return self.repository.find_all()
        return self.repository.find_by_status(status)

    def update_task(self, task_id: int, new_description: str) -> Task:
        """
        Update task description

        Args:
            task_id: Task ID to update
            new_description: New task description

        Returns:
            Updated task
        """
        if not new_description or not new_description.strip():
            raise ValueError("Description cannot be empty")

        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with id {task_id} not found")

        task.update_description(new_description.strip())
        self.repository.update_task(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete task by id

        Args:
            task_id: Task ID to delete

        Returns:
            True if task was deleted, False otherwise
        """
        task = self.repository.find_by_id(task_id)

        if not task:
            raise ValueError(f"Task with id {task_id} not found")

        return self.repository.delete_task(task_id)

    def mark_task_todo(self, task_id: int) -> Task:
        """
        Mark task as todo

        Args:
            task_id: Task ID to mark as todo

        Returns:
            Marked task
        """
        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        task.update_status("todo")
        self.repository.update_task(task)
        return task

    def mark_task_in_progress(self, task_id: int) -> Task:
        """
        Mark task as in progress

        Args:
            task_id: Task ID to mark as in progress

        Returns:
            Marked task
        """
        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        task.update_status("in-progress")
        self.repository.update_task(task)
        return task

    def mark_task_done(self, task_id: int) -> Task:
        """
        Mark task as done

        Args:
            task_id: Task ID to mark as done

        Returns:
            Marked task
        """
        task = self.repository.find_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        task.update_status("done")
        self.repository.update_task(task)
        return task
