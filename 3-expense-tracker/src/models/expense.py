from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Expense:
    """
    Expense data model.
    Attributes:
        id (int): The unique identifier of the expense.
        amount (float): The amount of the expense.
        date (datetime): The date of the expense.
        category (Optional[str]): The category of the expense.
    """

    id: int
    amount: float
    date: datetime
    category: Optional[str] = None


@dataclass
class ExpenseSummary:
    """
    Expense summary data model.
    Attributes:
        total (float): The total amount of the expenses.
        count (int): The number of expenses.
        period (str): The period of the expenses.
    """

    total: float
    count: int
    period: str
