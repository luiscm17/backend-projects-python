"""
Service for business logic of expenses.
This service handles the core functionality of the expense tracker,
including adding, retrieving, and summarizing expenses.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from models.expense import Expense, ExpenseSummary
from models.storage import StorageInterface
from models.exceptions import ExpenseNotFoundError
from services.validation import ValidationService
from utils.date_utils import DateUtils


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
        date: Optional[datetime] = None,
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

    def get_expenses_by_date_range(
        self, start_date: datetime, end_date: datetime
    ) -> List[Expense]:
        """
        Get expenses in a range of dates.
        Args:
            start_date: The start date.
            end_date: The end date.
        Returns:
            List[Expense]: The expenses in the range of dates.
        """
        expenses = self.list_expenses()
        return [e for e in expenses if start_date <= e.date <= end_date]

    def get_expenses_by_month(self, year: int, month: int) -> List[Expense]:
        """
        Get expenses in a specific month.
        Args:
            year: The year.
            month: The month.
        Returns:
            List[Expense]: The expenses in the month.
        """
        start_date, end_date = DateUtils.get_month_range(year, month)
        return self.get_expenses_by_date_range(start_date, end_date)

    def get_monthly_summary(self, year: int, month: int) -> ExpenseSummary:
        """
        Get a monthly resume datailed
        """
        expenses = self.get_expenses_by_month(year, month)
        total = sum(e.amount for e in expenses)

        month_name = datetime(year, month, 1).strftime("%B")
        period = f"Month {month}"

        return ExpenseSummary(total=total, count=len(expenses), period=period)

    def get_yearly_summary(self, year: int) -> ExpenseSummary:
        """
        Get yearly summary.

        Args:
            year: Year

        Returns:
            ExpenseSummary: Summary of the year
        """
        start_date, end_date = DateUtils.get_year_range(year)
        expenses = self.get_expenses_by_date_range(start_date, end_date)
        total = sum(e.amount for e in expenses)

        return ExpenseSummary(total=total, count=len(expenses), period=f"Year {year}")

    def get_last_n_days_summary(self, days: int) -> ExpenseSummary:
        """
        Get summary of the last N days.

        Args:
            days: Number of days

        Returns:
            ExpenseSummary: Summary of the period
        """
        start_date, end_date = DateUtils.get_last_n_days(days)
        expenses = self.get_expenses_by_date_range(start_date, end_date)
        total = sum(e.amount for e in expenses)

        return ExpenseSummary(
            total=total, count=len(expenses), period=f"Last {days} days"
        )

    def search_expenses(self, query: str) -> List[Expense]:
        """
        Search expenses by description.

        Args:
            query: Search term

        Returns:
            List[Expense]: Expenses that match the search term
        """
        expenses = self.list_expenses()
        query_lower = query.lower()

        return [e for e in expenses if query_lower in e.description.lower()]

    def get_expense_statistics(
        self, expenses: Optional[List[Expense]] = None
    ) -> Dict[str, Any]:
        """
        Get detailed statistics of expenses.

        Args:
            expenses: List of expenses (optional, uses all if not provided)

        Returns:
            Dict[str, Any]: Detailed statistics of expenses
        """
        if expenses is None:
            expenses = self.list_expenses()

        if not expenses:
            return {
                "total": 0.0,
                "count": 0,
                "average": 0.0,
                "max": 0.0,
                "min": 0.0,
                "median": 0.0,
            }

        amounts = [e.amount for e in expenses]
        amounts_sorted = sorted(amounts)

        # Calculate median
        n = len(amounts_sorted)
        if n % 2 == 0:
            median = (amounts_sorted[n // 2 - 1] + amounts_sorted[n // 2]) / 2
        else:
            median = amounts_sorted[n // 2]

        return {
            "total": sum(amounts),
            "count": len(expenses),
            "average": sum(amounts) / len(expenses),
            "max": max(amounts),
            "min": min(amounts),
            "median": median,
        }
