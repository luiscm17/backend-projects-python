"""
Validation service for expense tracker.

This module provides validation logic for expense data entries.
"""

import re
from typing import Any
from models.exceptions import ValidationError


class ValidationService:
    """
    Validation service for expense tracker.

    This class provides validation logic for expense data entries.
    """

    @staticmethod
    def validate_amount(amount: Any) -> float:
        """
        Validate and convert amount to float.

        Args:
            amount: The amount to validate

        Returns:
            float: The validated amount as float

        Raises:
            ValidationError: If amount is invalid
        """
        try:
            amount_float = float(amount)
        except (ValueError, TypeError):
            raise ValidationError("amount", str(amount), "must be a number")
        if amount_float <= 0:
            raise ValidationError("amount", str(amount_float), "must be post")

        return amount_float

    @staticmethod
    def validate_description(description: Any) -> str:
        """
        Validate and clean description string.

        Args:
            description: The description to validate

        Returns:
            str: The validated and cleaned description

        Raises:
            ValidationError: If description is invalid
        """
        if not description:
            raise ValidationError("description", str(description), "cannot be empty")

        description_str = str(description).strip()
        if not description_str:
            raise ValidationError(
                "description",
                str(description),
                "cannot be empty after trimming whitespace",
            )

        if len(description_str) > 255:
            raise ValidationError(
                "description", str(description_str), "too long (max 255 characters)"
            )

        if not re.match(r"^[a-zA-Z0-9\s\-_.,!?]+$", description_str):
            raise ValidationError(
                "description", description_str, "contains invalid characters"
            )

        return description_str

    @staticmethod
    def validate_expense_id(expense_id: Any) -> int:
        """
        Validate and convert expense ID to integer.

        Args:
            expense_id: The expense ID to validate

        Returns:
            int: The validated expense ID as integer

        Raises:
            ValidationError: If expense ID is invalid
        """
        try:
            expense_id_int = int(expense_id)
        except (ValueError, TypeError):
            raise ValidationError("id", str(expense_id), "must be a integer")

        if expense_id_int <= 0:
            raise ValidationError("id", str(expense_id_int), "must be positive")

        return expense_id_int

    @staticmethod
    def validate_month(month: Any) -> int:
        """
        Validate and convert month to integer.

        Args:
            month: The month to validate

        Returns:
            int: The validated month as integer

        Raises:
            ValidationError: If month is invalid
        """
        try:
            month_int = int(month)
        except (ValueError, TypeError):
            raise ValidationError("month", str(month), "must be an integer")
        if month_int < 1 or month_int > 12:
            raise ValidationError("month", str(month_int), "must be between 1 and 12")

        return month_int
