from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Expense:
    id: int
    amount: float
    date: datetime
    category: Optional[str] = None


@dataclass
class ExpenseSummary:
    total: float
    count: int
    period: str
