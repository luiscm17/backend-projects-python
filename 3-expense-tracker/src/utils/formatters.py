"""
Output formatters for expense tracker.

This module provides functions to format expense data for output.
"""

from typing import List, Dict, Any
from datetime import datetime
from models.expense import Expense, ExpenseSummary
from utils.date_utils import DateUtils


class OutputFormatter:
    """Main class for output formatters."""

    COLORS = {
        "header": "\033[95m",
        "ok_blue": "\033[94m",
        "ok_green": "\033[92m",
        "warning": "\033[93m",
        "fail": "\033[91m",
        "end_color": "\033[0m",
        "bold": "\033[1m",
        "underline": "\033[4m",
    }

    @classmethod
    def colorize(cls, text: str, color: str) -> str:
        """
        Apply color to a text.

        Args:
            text: Text to color
            color: Color name

        Returns:
            str: Text colored
        """
        if color in cls.COLORS:
            return f"{cls.COLORS[color]}{text}{cls.COLORS['end_color']}"
        return text

    @classmethod
    def format_expense_table(
        cls, expenses: List[Expense], show_colors: bool = True
    ) -> str:
        """
        Format a list of expenses as a table.

        Args:
            expenses: List of expenses
            show_colors: If use colors in the output

        Returns:
            str: Formatted table
        """
        if not expenses:
            return (
                cls.colorize("No expenses found.", "warning")
                if show_colors
                else "No expenses found."
            )

        # Sort expenses by date (most recent first)
        expenses_sorted = sorted(expenses, key=lambda x: x.date, reverse=True)

        # Calculate column widths
        id_width = max(3, max(len(str(e.id)) for e in expenses_sorted))
        date_width = 12
        desc_width = max(11, min(30, max(len(e.description) for e in expenses_sorted)))
        amount_width = 12

        # Header
        header_parts = [
            f"{'ID':<{id_width}}",
            f"{'Date':<{date_width}}",
            f"{'Description':<{desc_width}}",
            f"{'Amount':>{amount_width}}",
        ]
        header = " ".join(header_parts)

        if show_colors:
            header = cls.colorize(header, "header")

        # Separator line
        separator = "-" * len(header)

        # Rows
        rows = []
        total = 0.0

        for expense in expenses_sorted:
            date_str = expense.date.strftime("%Y-%m-%d")
            amount_str = f"${expense.amount:.2f}"

            # Truncate description if too long
            description = expense.description
            if len(description) > desc_width:
                description = description[: desc_width - 3] + "..."

            # Format amount with color based on value
            if show_colors:
                if expense.amount > 100:
                    amount_str = cls.colorize(amount_str, "fail")
                elif expense.amount > 50:
                    amount_str = cls.colorize(amount_str, "warning")
                else:
                    amount_str = cls.colorize(amount_str, "ok_green")

            row_parts = [
                f"{expense.id:<{id_width}}",
                f"{date_str:<{date_width}}",
                f"{description:<{desc_width}}",
                f"{amount_str:>{amount_width}}",
            ]
            rows.append(" ".join(row_parts))

            total += expense.amount

        # Total
        total_str = f"${total:.2f}"
        if show_colors:
            total_str = cls.colorize(total_str, "bold")

        total_row = (
            f"{'':<{id_width + date_width + desc_width + 1}}{total_str:>{amount_width}}"
        )

        return "\n".join([header, separator] + rows + [separator, total_row])

    @classmethod
    def format_summary(
        cls,
        summary: ExpenseSummary,
        show_details: bool = False,
        show_colors: bool = True,
    ) -> str:
        """
        Format an improved expense summary.

        Args:
            summary: Expense summary
            show_details: If show additional details
            show_colors: If use colors

        Returns:
            str: Formatted summary
        """
        lines = []

        # Title
        if summary.period.startswith("Month"):
            month_num = int(summary.period.split()[1])
            month_name = datetime(2024, month_num, 1).strftime("%B")
            title = f"Expense Summary - {month_name}"
        else:
            title = "Expense Summary - All Time"

        if show_colors:
            title = cls.colorize(title, "header")

        lines.append(title)
        lines.append("=" * len(title))

        # Main stats
        total_str = f"${summary.total:.2f}"
        count_str = f"{summary.count} expense{'s' if summary.count != 1 else ''}"

        if show_colors:
            total_str = cls.colorize(total_str, "bold")

        lines.append(f"Total: {total_str}")
        lines.append(f"Count: {count_str}")

        if summary.count > 0:
            avg = summary.total / summary.count
            avg_str = f"${avg:.2f}"
            lines.append(f"Average: {avg_str}")

        if show_details:
            lines.append("")
            lines.append("Tips:")
            if summary.total > 500:
                lines.append(
                    cls.colorize("  • Consider reviewing large expenses", "warning")
                    if show_colors
                    else "  • Consider reviewing large expenses"
                )
            if summary.count > 20:
                lines.append(
                    cls.colorize(
                        "  • Many small expenses - consider budgeting", "ok_blue"
                    )
                    if show_colors
                    else "  • Many small expenses - consider budgeting"
                )

        return "\n".join(lines)

    @classmethod
    def format_expense_details(cls, expense: Expense, show_colors: bool = True) -> str:
        """
        Format the details of an individual expense.

        Args:
            expense: Expense to format
            show_colors: If use colors

        Returns:
            str: Formatted details
        """
        lines = []

        # Title
        title = f"Expense Details - ID: {expense.id}"
        if show_colors:
            title = cls.colorize(title, "header")

        lines.append(title)
        lines.append("=" * len(title))
        lines.append("")

        # Expense information
        lines.append(f"Description: {expense.description}")
        lines.append(
            f"Amount: {cls.colorize(f'${expense.amount:.2f}', 'bold') if show_colors else f'${expense.amount:.2f}'}"
        )
        lines.append(f"Date: {expense.date.strftime('%A, %B %d, %Y at %I:%M %p')}")

        if expense.category:
            lines.append(f"Category: {expense.category}")

        # Additional information
        lines.append("")
        lines.append("Date Information:")
        lines.append(f" • Day of week: {expense.date.strftime('%A')}")
        lines.append(f" • Week of year: {expense.date.isocalendar()[1]}")
        lines.append(f" • Quarter: Q{(expense.date.month - 1) // 3 + 1}")

        return "\n".join(lines)


def format_expense_table(expenses: List[Expense]) -> str:
    """
    Format a list of expenses as a table.
    """
    return OutputFormatter.format_expense_table(expenses)


def format_summary(summary: ExpenseSummary) -> str:
    """
    Format an expense summary.
    """
    return OutputFormatter.format_summary(summary)
