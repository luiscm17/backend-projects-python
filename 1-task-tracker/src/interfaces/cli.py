from typing import List
from src.models.task import Task


class TaskCommands:
    @staticmethod
    def format_task_list(tasks: List[Task]) -> str:
        if not tasks:
            return "No tasks found"

        output = []
        for task in tasks:
            output.append(f"ID: {task.id}")
            output.append(f"Description: {task.description}")
            output.append(f"Status: {task.status}")
            output.append(f"Created: {task.created_at}")
            output.append("-" * 20)

        return "\n".join(output)
