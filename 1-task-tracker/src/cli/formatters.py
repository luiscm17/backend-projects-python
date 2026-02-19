from typing import List
from src.models.task import Task


class TaskFormatter:
    @staticmethod
    def format_task_list(tasks: List[Task]) -> str:
        """
        Format a list of tasks into a readable string.

        Args:
            tasks: A list of Task objects

        Returns:
            A formatted string containing all tasks
        """
        if not tasks:
            return "No tasks found"

        output = []
        for task in tasks:
            output.append(f"ID: {task.id}")
            output.append(f"Description: {task.description}")
            output.append(f"Status: {task.status}")
            output.append(f"Created at: {task.created_at}")
            output.append(f"Updated at: {task.updated_at}")
            output.append("")

        return "\n".join(output)

    @staticmethod
    def format_success_message(action: str, task_id: int) -> str:
        """
        Format a success message for a task operation.

        Args:
            action: The action performed (add, update, delete, todo, in-progress, done)
            task_id: The ID of the task

        Returns:
            A formatted success message string
        """
        message = {
            "add": f"Task ID:{task_id} added successfully",
            "update": f"Task ID:{task_id} updated successfully",
            "delete": f"Task ID:{task_id} deleted successfully",
            "todo": f"Task ID:{task_id} marked as todo",
            "in-progress": f"Task ID:{task_id} marked as in progress",
            "done": f"Task ID:{task_id} marked as done",
        }
        return message.get(action, f"Task ID:{task_id} {action} successfully")
