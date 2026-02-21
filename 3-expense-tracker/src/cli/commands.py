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
from utils.formatters import format_expense_table, format_summary


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
        if not expenses:
            print("No expenses found")
            return
        print(format_expense_table(expenses))
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
        summary = service.get_summary(args.month if hasattr(args, "month") else None)
        print(format_summary(summary))
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
        expense = service.update_expense(
            args.id,
            args.descripción if hasattr(args, "description") else None,
            args.amount if hasattr(args, "amount") else None,
        )
        print("Expense updated successfully")
    except ExpenseTrackerError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
