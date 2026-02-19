import sys
from typing import List, Dict
from src.container.di_container import DIContainer
from src.cli.validators import ArgumentValidator


class TaskCLI:
    """Main CLI application class with dependency injection"""

    def __init__(self, container: DIContainer = None):
        self.container = container or DIContainer()
        self.commands = self._register_commands()

    def _register_commands(self) -> Dict[str, any]:
        """
        Register all available commands using DI container

        Returns:
            Dictionary of command names to command instances
        """
        return {
            "add": self.container.create_command("add"),
            "update": self.container.create_command("update"),
            "delete": self.container.create_command("delete"),
            "list": self.container.create_command("list"),
            "todo": self.container.create_command("todo"),
            "in-progress": self.container.create_command("in-progress"),
            "done": self.container.create_command("done"),
        }

    def _show_usage(self) -> None:
        """
        Show usage information
        """
        print("Usage: task-cli <command> [arguments]")
        print("Available commands:")
        print(" add <description>       - Add a new task")
        print(" update <id> <description> - Update a task")
        print(" delete <id>             - Delete a task")
        print(" list [status]           - List all tasks")
        print(" list all                - List all tasks")
        print(" list todo               - List tasks with todo status")
        print(" list in-progress        - List tasks with in-progress status")
        print(" list done               - List tasks with done status")
        print(" todo <id>               - Mark a task as todo")
        print(" in-progress <id>        - Mark a task as in progress")
        print(" done <id>               - Mark a task as done")

    def run(self, args: List[str]) -> None:
        """
        Run the CLI application

        Args:
            args: List of command line arguments
        """
        if len(args) < 2:
            self._show_usage()
            return

        command = args[1]

        if command in self.commands:
            self.commands[command].execute(args)
        else:
            print(f"Unknown command: {command}")
            self._show_usage()
