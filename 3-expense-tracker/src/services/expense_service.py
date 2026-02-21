"""
Service for business logic of expenses.
This service handles the core functionality of the expense tracker,
including adding, retrieving, and summarizing expenses.
"""

from datetime import datetime
from typing import List, Optional
from models.expense import Expense, ExpenseSummary
from models.storage import StorageInterface
from models.exceptions import ExpenseNotFoundError, InvalidExpenseError
from services.validation import ValidationService


class ExpenseService:
    """
    Service responsible for the business logic of expenses
    """

    def __init__(self, storage: StorageInterface):
        """
        Initialize the expense service.

        Args:
            storage: The storage interface to use.
        """
        self._storage = storage
        self._validator = ValidationService()

    def add_expense(self, description: str, amount: float) -> Expense:
        """
        Add a new expense to the storage.

        Args:
            description: The description of the expense.
            amount: The amount of the expense.

        Returns:
            The created expense.
        """
        validated_description = self._validator.validate_description(description)
        validated_amount = self._validator.validate_amount(amount)

        expenses = self._storage.get_all_expenses()
        new_id = max([e.id for e in expenses], default=0) + 1

        expense = Expense(
            id=new_id,
            description=validated_description,
            amount=validated_amount,
            date=datetime.now(),
        )

        return self._storage.save_expense(expense)

    def get_expense(self, expense_id: int) -> Expense:
        """
        Get an expense by ID.

        Args:
            expense_id: The ID of the expense to retrieve.

        Returns:
            The expense with the given ID.

        Raises:
            ExpenseNotFoundError: If the expense is not found.
        """
        validated_id = self._validator.validate_expense_id(expense_id)

        expense = self._storage.get_expense(validated_id)
        if expense is None:
            raise ExpenseNotFoundError(validated_id)
        return expense

    def list_expenses(self) -> List[Expense]:
        """
        List all expenses.

        Returns:
            A list of all expenses.
        """
        return self._storage.get_all_expenses()

    def delete_expense(self, expense_id: int) -> None:
        """
        Delete an expense by ID.

        Args:
            expense_id: The ID of the expense to delete.

        Raises:
            ExpenseNotFoundError: If the expense is not found.
        """

        validated_id = self._validator.validate_expense_id(expense_id)

        self.get_expense(validated_id)

        success = self._storage.delete_expense(validated_id)
        if not success:
            raise ExpenseNotFoundError(validated_id)

    def update_expense(
        self,
        expense_id: int,
        description: Optional[str] = None,
        amount: Optional[float] = None,
    ) -> Expense:
        """
        Update an expense.

        Args:
            expense_id: The ID of the expense to update.
            description: The new description of the expense.
            amount: The new amount of the expense.

        Returns:
            The updated expense.

        Raises:
            ExpenseNotFoundError: If the expense is not found.
        """

        validated_id = self._validator.validate_expense_id(expense_id)

        expense = self.get_expense(validated_id)

        if amount is not None:
            expense.description = self._validator.validate_description(description)

        if amount is not None:
            expense.amount = self._validator.validate_amount(amount)
        return self._storage.update_expense(expense)

    def get_summary(self, month: Optional[int] = None) -> ExpenseSummary:
        """
        Get a summary of expenses.

        Args:
            month: The month to filter by.

        Returns:
            The summary of expenses.
        """
        expenses = self.list_expenses()

        if month is not None:
            validated_month = int(self._validator.validate_amount(month))
            expenses = [e for e in expenses if e.date.month == validated_month]
            period = f"Month {validated_month}"
        else:
            period = "All time"

        total = sum(e.amount for e in expenses)

        return ExpenseSummary(total=total, count=len(expenses), period=period)
