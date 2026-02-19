from typing import List, Optional


class ArgumentValidator:
    @staticmethod
    def validate_task_id(args: List[str]) -> Optional[int]:
        """
        Validate that a task ID is provided and is a number.

        Args:
            args: The command line arguments

        Returns:
            The task ID as an integer, or None if validation fails
        """
        if len(args) < 3:
            print("Error: Task ID is required")
            return None
        try:
            return int(args[2])
        except ValueError:
            print("Error: Task ID must be a number")
            return None

    @staticmethod
    def validate_description(args: List[str]) -> Optional[str]:
        """
        Validate that a description is provided and is not empty.

        Args:
            args: The command line arguments

        Returns:
            The description as a string, or None if validation fails
        """
        if len(args) < 3:
            print("Error: Description is required")
            return None

        description = " ".join(args[2:])
        if not description.strip():
            print("Error: Description cannot be empty")
            return None

        return description.strip()

    @staticmethod
    def validate_list_args(args: List[str]) -> Optional[str]:
        """
        Validate that a list argument is provided and is valid.

        Args:
            args: The command line arguments

        Returns:
            The list argument as a string, or None if validation fails
        """
        if len(args) >= 3:
            return args[2].lower()
        return None
