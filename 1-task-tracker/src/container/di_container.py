"""
Dependency Injection Container

Centralized dependency management for the Task Tracker application.
Provides lazy loading and singleton pattern for all services.
SQLite-only implementation.
"""

from typing import Dict, Type
from src.utils.db_handler import DBHandler
from src.repositories.task_repository_db import TaskRepositoryDB
from src.services.task_service import TaskService
from src.cli.formatters import TaskFormatter
from src.cli.commands import (
    BaseCommand,
    AddCommand,
    UpdateCommand,
    DeleteCommand,
    ListCommand,
    TodoCommand,
    InProgressCommand,
    DoneCommand,
)


class DIContainer:
    """
    Dependency Injection Container

    Manages creation and lifecycle of all application dependencies.
    Implements lazy loading and singleton pattern.
    SQLite-only implementation.
    """

    def __init__(self):
        self._db_handler = None
        self._repository = None
        self._service = None
        self._formatter = None
        self._commands: Dict[str, BaseCommand] = {}

    @property
    def db_handler(self) -> DBHandler:
        """Get or create DBHandler instance (lazy loading)"""
        if self._db_handler is None:
            self._db_handler = DBHandler()
        return self._db_handler

    @property
    def repository(self) -> TaskRepositoryDB:
        """Get or create TaskRepository instance (lazy loading)"""
        if self._repository is None:
            self._repository = TaskRepositoryDB(self.db_handler)
        return self._repository

    @property
    def service(self) -> TaskService:
        """Get or create TaskService instance (lazy loading)"""
        if self._service is None:
            self._service = TaskService(self.repository)
        return self._service

    @property
    def formatter(self) -> TaskFormatter:
        """Get or create TaskFormatter instance (lazy loading)"""
        if self._formatter is None:
            self._formatter = TaskFormatter()
        return self._formatter

    def create_command(self, command_type: str) -> BaseCommand:
        """
        Factory method for creating commands with injected dependencies

        Args:
            command_type: Type of command to create

        Returns:
            Command instance with dependencies injected

        Raises:
            ValueError: If command type is unknown
        """
        command_classes: Dict[str, Type[BaseCommand]] = {
            "add": AddCommand,
            "update": UpdateCommand,
            "delete": DeleteCommand,
            "list": ListCommand,
            "todo": TodoCommand,
            "in-progress": InProgressCommand,
            "done": DoneCommand,
        }

        command_class = command_classes.get(command_type)
        if command_class is None:
            raise ValueError(f"Unknown command: {command_type}")

        # Create command with injected dependencies
        return command_class(service=self.service, formatter=self.formatter)

    def get_all_commands(self) -> Dict[str, BaseCommand]:
        """
        Get all available commands with dependencies injected

        Returns:
            Dictionary mapping command names to command instances
        """
        if not self._commands:
            command_types = [
                "add",
                "update",
                "delete",
                "list",
                "todo",
                "in-progress",
                "done",
            ]

            for command_type in command_types:
                self._commands[command_type] = self.create_command(command_type)

        return self._commands

    def reset(self) -> None:
        """Reset all cached instances (useful for testing)"""
        self._db_handler = None
        self._repository = None
        self._service = None
        self._formatter = None
        self._commands = {}
