import argparse
from re import sub
from cli.commands import cmd_add, cmd_delete, cmd_list, cmd_summary, cmd_update


def create_parser() -> argparse.ArgumentParser:
    """
    Create a parser for the command line arguments.
    Returns:
        argparse.ArgumentParser: The parser.
    """
    parser = argparse.ArgumentParser(
        prog="expense-tracker", description="A simple CLI expense tracker"
    )

    subparser = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparser.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, help="Expense description")
    add_parser.add_argument(
        "--amount", required=True, type=float, help="Expense amount"
    )
    add_parser.set_defaults(func=cmd_add)

    # List command
    list_parser = subparser.add_parser("list", help="List all expenses")
    list_parser.set_defaults(func=cmd_list)

    # Delete command
    delete_parser = subparser.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int, help="Expense ID")
    delete_parser.set_defaults(func=cmd_delete)

    # Summary command
    summary_parser = subparser.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=int, required=True, help="Month (1-12)")
    summary_parser.set_defaults(func=cmd_summary)

    # Update command
    update_parser = subparser.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", required=True, type=int, help="Expense ID")
    update_parser.add_argument("--description", help="New description")
    update_parser.add_argument("--amount", type=float, help="New amount")
    update_parser.set_defaults(func=cmd_update)

    return parser
