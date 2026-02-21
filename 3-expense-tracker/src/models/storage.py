from abc import ABC, abstractmethod
from typing import List, Optional
from models.expense import Expense


class StorageInterface(ABC):
    """
    Storage interface for expenses.
    """

    @abstractmethod
    def save_expense(self, expense: Expense) -> Expense:
        """
        Save an expense to the storage.
        """
        pass

    @abstractmethod
    def get_expense(self, id: int) -> Optional[Expense]:
        """
        Get an expense by id.
        """
        pass

    @abstractmethod
    def get_all_expenses(self) -> List[Expense]:
        """
        Get all expenses.
        """
        pass

    @abstractmethod
    def update_expense(self, expense: Expense) -> Expense:
        """
        Update an expense.
        """
        pass

    @abstractmethod
    def delete_expense(self, id: int) -> bool:
        """
        Delete an expense by id.
        """
        pass
