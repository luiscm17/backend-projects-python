"""
CLI Commands Handler
This module contains the command handlers for the CLI.
"""

import sys
from datetime import datetime
from typing import Dict, Any
from services.expense_service import ExpenseService
from models.storage import JsonStorage
from models.exceptions import ExpenseTrackerError
from utils.formatters import format_expense_table, format_summary, OutputFormatter


def get_service() -> ExpenseService:
    storage = JsonStorage()
    return ExpenseService(storage)


def cmd_add(args: Dict[str, Any]) -> None:
    """
    Add a new expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    try:
        service = get_service()
        expense = service.add_expense(args.description, args.amount)
        print(f"Expense added successfully with ID: {expense.id}")
    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_list(args: Dict[str, Any]) -> None:
    """
    List all expenses.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    try:
        service = get_service()
        expenses = service.list_expenses()

        if hasattr(args, "month") and args.month:
            year = (
                args.year
                if hasattr(args, "year") and args.year
                else datetime.now().year
            )
            expenses = service.get_expenses_by_month(year, args.month)

        if hasattr(args, "search") and args.search:
            expenses = service.search_expenses(args.search)

        expenses = sorted(expenses, key=lambda x: x.date, reverse=True)

        if hasattr(args, "limit") and args.limit:
            expenses = expenses[: args.limit]

        if not expenses:
            print("No expenses found.")
            return

        show_colors = not getattr(args, "no_color", False)
        print(OutputFormatter.format_expense_table(expenses, show_colors))

    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args: Dict[str, Any]) -> None:
    """
    Delete an expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    try:
        service = get_service()
        service.delete_expense(args.id)
        print(f"Expense with ID {args.id} was deleted successfully")
    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_summary(args: Dict[str, Any]) -> None:
    """
    Show expense summary.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    try:
        service = get_service()
        show_colors = not getattr(args, "no_color", False)
        show_details = getattr(args, "detailed", False)

        if hasattr(args, "days") and args.days:
            summary = service.get_last_n_days_summary(args.days)
        elif hasattr(args, "month") and args.month:
            year = (
                args.year
                if hasattr(args, "year") and args.year
                else datetime.now().year
            )
            summary = service.get_monthly_summary(year, args.month)
        elif hasattr(args, "year") and args.year:
            summary = service.get_yearly_summary(args.year)
        else:
            summary = service.get_summary()

        print(OutputFormatter.format_summary(summary, show_details, show_colors))

    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_update(args: Dict[str, Any]) -> None:
    """
    Update an expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    try:
        service = get_service()

        update_params = {"expense_id": args.id}

        if hasattr(args, "description") and args.description:
            update_params["description"] = args.description

        if hasattr(args, "amount") and args.amount:
            update_params["amount"] = args.amount

        if hasattr(args, "category") and args.category:
            update_params["category"] = args.category

        expense = service.update_expense(**update_params)
        print("Expense updated successfully")
        print(
            f"ID: {expense.id}, Description: {expense.description}, Amount: ${expense.amount:.2f}"
        )

    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_show(args: Dict[str, Any]) -> None:
    """Handler para el comando show."""
    try:
        service = get_service()
        expense = service.get_expense(args.id)

        show_colors = not getattr(args, "no_color", False)
        print(OutputFormatter.format_expense_details(expense, show_colors))

    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_stats(args: Dict[str, Any]) -> None:
    """Handler para el comando stats."""
    try:
        service = get_service()

        expenses = service.list_expenses()

        if hasattr(args, "month") and args.month:
            year = (
                args.year
                if hasattr(args, "year") and args.year
                else datetime.now().year
            )
            expenses = service.get_expenses_by_month(year, args.month)

        if not expenses:
            print("No expenses found for the specified period.")
            return

        stats = service.get_expense_statistics(expenses)

        print("Expense Statistics")
        print("=" * 20)
        print(f"Total: ${stats['total']:.2f}")
        print(f"Count: {stats['count']}")
        print(f"Average: ${stats['average']:.2f}")
        print(f"Maximum: ${stats['max']:.2f}")
        print(f"Minimum: ${stats['min']:.2f}")
        print(f"Median: ${stats['median']:.2f}")

    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
