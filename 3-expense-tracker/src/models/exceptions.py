"""
Custom exceptions for the expense tracker.

This module defines custom exceptions that are used throughout the application
to handle specific error conditions in a consistent manner.
"""


class ExpenseTrackerError(Exception):
    """
    Base exception for the expense tracker.
    """

    pass


class ExpenseNotFoundError(ExpenseTrackerError):
    """
    Exception raised when an expense is not found.
    """

    def __init__(self, expense_id: int):
        self.expense_id = expense_id
        super().__init__(f"Expense with id {expense_id} not found")


class InvalidExpenseError(ExpenseTrackerError):
    """
    Exception raised when an expense is invalid.
    """

    def __init__(self, message: str):
        super().__init__(f"Invalid expense data: {message}")


class RepositoryError(ExpenseTrackerError):
    """
    Exception raised when there is an error with the repository.
    """

    def __init__(self, message: str):
        super().__init__(f"Repository error: {message}")


class ValidationError(ExpenseTrackerError):
    """
    Exception raised when there is a validation error.
    """

    def __init__(self, field: str, value: str, reason: str):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(
            f"Validation error: {field} with value {value} is invalid: {reason}"
        )
