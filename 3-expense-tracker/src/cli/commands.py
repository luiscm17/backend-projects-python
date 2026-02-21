from ast import arg
from calendar import month
from datetime import datetime
from typing import Dict, Any


def cmd_add(args: Dict[str, Any]) -> None:
    """
    Add a new expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    print(f"Adding expense: {args.description} - ${args.amount}")
    print(f"Expense added successfully")


def cmd_list(args: Dict[str, Any]) -> None:
    """
    List all expenses.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    print("ID   | Date      | Description   | Amount")
    print("-" * 50)
    print("1    | 2022-01-01| Test            | 10")
    print("2    | 2022-01-02| Test            | 20")


def cmd_delete(args: Dict[str, Any]) -> None:
    """
    Delete an expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    print(f"Deleting expense with id: {args.id}")
    print(f"Expense deleted successfully")


def cmd_summary(args: Dict[str, Any]) -> None:
    """
    Show expense summary.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    if args.month:
        month_name = datetime(2024, args.month, 1).strftime("&B")
        print(f"Total expenses for {month_name}: $10")
    else:
        print("Total expenses: $20")


def cmd_update(args: Dict[str, Any]) -> None:
    """
    Update an expense.
    Args:
        args (Dict[str, Any]): The command line arguments.
    """
    print(f"Updating expense with id: {args.id}")
    print(f"Expense updated successfully")
