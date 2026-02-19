from abc import ABC, abstractmethod
from typing import List
from src.services.task_service import TaskService
from src.cli.validators import ArgumentValidator
from src.cli.formatters import TaskFormatter


class BaseCommand(ABC):
    """Base class for all CLI commands"""

    def __init__(self, service: TaskService, formatter: TaskFormatter):
        self.service = service
        self.formatter = formatter

    @abstractmethod
    def execute(self, args: List[str]) -> None:
        pass


class AddCommand(BaseCommand):
    """Command to add a new task"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the add command.

        Args:
            args: List of command line arguments
        """
        description = ArgumentValidator.validate_description(args)
        if description is None:
            return

        try:
            task = self.service.add_task(description)
            print(self.formatter.format_success_message("add", task.id))
        except ValueError as e:
            print(f"Error: {str(e)}")


class UpdateCommand(BaseCommand):
    """Command to update a task description"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the update command.

        Args:
            args: List of command line arguments
        """
        if len(args) < 4:
            print("Error: Task ID and new description are required")
            return

        task_id = ArgumentValidator.validate_task_id(args)
        new_description = ArgumentValidator.validate_description(args[2:])
        if task_id is None or new_description is None:
            return

        try:
            self.service.update_task(task_id, new_description)
            print(self.formatter.format_success_message("update", task_id))
        except ValueError as e:
            print(f"Error: {str(e)}")


class DeleteCommand(BaseCommand):
    """Command to delete a task"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the delete command.

        Args:
            args: List of command line arguments
        """
        task_id = ArgumentValidator.validate_task_id(args)
        if task_id is None:
            return

        try:
            self.service.delete_task(task_id)
            print(self.formatter.format_success_message("delete", task_id))
        except ValueError as e:
            print(f"Error: {str(e)}")


class ListCommand(BaseCommand):
    """Command to list tasks"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the list command.

        Args:
            args: List of command line arguments
        """
        status_filter = ArgumentValidator.validate_list_args(args)

        try:
            if status_filter:
                tasks = self.service.list_tasks_by_status(status_filter)
            else:
                tasks = self.service.list_all_tasks()

            print(self.formatter.format_task_list(tasks))
        except ValueError as e:
            print(f"Error: {str(e)}")


class TodoCommand(BaseCommand):
    """Command to mark a task as todo"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the todo command.

        Args:
            args: List of command line arguments
        """
        task_id = ArgumentValidator.validate_task_id(args)
        if task_id is None:
            return

        try:
            self.service.mark_task_todo(task_id)
            print(self.formatter.format_success_message("todo", task_id))
        except ValueError as e:
            print(f"Error: {str(e)}")


class InProgressCommand(BaseCommand):
    """Command to mark a task as in progress"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the in progress command.

        Args:
            args: List of command line arguments
        """
        task_id = ArgumentValidator.validate_task_id(args)
        if task_id is None:
            return

        try:
            self.service.mark_task_in_progress(task_id)
            print(self.formatter.format_success_message("in progress", task_id))
        except ValueError as e:
            print(f"Error: {str(e)}")


class DoneCommand(BaseCommand):
    """Command to mark a task as done"""

    def execute(self, args: List[str]) -> None:
        """
        Execute the done command.

        Args:
            args: List of command line arguments
        """
        task_id = ArgumentValidator.validate_task_id(args)
        if task_id is None:
            return

        try:
            self.service.mark_task_done(task_id)
            print(self.formatter.format_success_message("done", task_id))
        except ValueError as e:
            print(f"Error: {str(e)}")
