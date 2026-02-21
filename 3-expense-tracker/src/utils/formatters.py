"""
Output formatters for expense tracker.

This module provides functions to format expense data for output.
"""

from typing import List
from models.expense import Expense, ExpenseSummary


def format_expense_table(expenses: List[Expense]) -> str:
    """
    Format a list of expenses as a table.

    Args:
        expenses: List of expenses

    Returns:
        str: Formatted table
    """
    if not expenses:
        return "No expenses found."

    # Header
    header = f"{'ID':<4} {'Date':<12} {'Description':<20} {'Amount':<10}"
    separator = "-" * len(header)

    # Rows
    rows = []
    for expense in expenses:
        date_str = expense.date.strftime("%Y-%m-%d")
        amount_str = f"${expense.amount:.2f}"

        # Truncate description if it's too long
        description = (
            expense.description[:17] + "..."
            if len(expense.description) > 20
            else expense.description
        )

        row = f"{expense.id:<4} {date_str:<12} {description:<20} {amount_str:<10}"
        rows.append(row)

    return "\n".join([header, separator] + rows)


def format_summary(summary: ExpenseSummary) -> str:
    """
    Format an expense summary.

    Args:
        summary: Expense summary

    Returns:
        str: Formatted summary
    """
    if summary.period.startswith("Month"):
        month_names = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        month_num = int(summary.period.split()[1])
        period_name = month_names[month_num]
        return f"Total expenses for {period_name}: ${summary.total:.2f}"
    else:
        return f"Total expenses: ${summary.total:.2f}"
