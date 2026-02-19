import sys
from typing import List, Dict
from src.cli.commands import *
from src.cli.validators import ArgumentValidator


class TaskCLI:
    def __init__(self):
        self.commands = self._register_commands()

    def _register_commands(self) -> Dict[str, BaseCommand]:
        return {
            "add": AddCommand(),
            "update": UpdateCommand(),
            "delete": DeleteCommand(),
            "list": ListCommand(),
            "todo": TodoCommand(),
            "in-progress": InProgressCommand(),
            "done": DoneCommand(),
        }

    def _show_usage(self) -> None:
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
        if len(args) < 2:
            self._show_usage()
            return

        command = args[1]

        if command in self.commands:
            self.commands[command].execute(args)
        else:
            print(f"Unknown command: {command}")
            self._show_usage()
