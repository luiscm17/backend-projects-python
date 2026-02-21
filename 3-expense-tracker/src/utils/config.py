"""
Configuration utilities for the expense tracker.

This module provides configuration constants and utility functions.
"""

from pathlib import Path
from typing import Final

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Final[Path] = BASE_DIR / "data"
EXPENSE_FILE: Final[Path] = DATA_DIR / "expenses.json"


def ensure_data_directory() -> None:
    """
    Ensure the data directory exists.
    """
    DATA_DIR.mkdir(exist_ok=True)


def get_expenses_file_path() -> Path:
    """
    Get the path to the expenses file.

    Returns:
        Path: The path to the expenses file
    """
    ensure_data_directory()
    return EXPENSE_FILE
