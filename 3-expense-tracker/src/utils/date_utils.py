from datetime import datetime, timedelta
from typing import Optional, Tuple
from calendar import monthrange, month_name


class DateUtils:
    """Utility class for date operations."""

    @staticmethod
    def get_current_month_range() -> Tuple[datetime, datetime]:
        """
        Get the range of the current month.
        Returns:
            Tuple[datetime, datetime]: A tuple containing the first day and last day of the current month.
        """
        now = datetime.now()
        first_day = datetime(now.year, now.month, 1)

        last_day_num = monthrange(now.year, now.month)[1]
        last_day = datetime(now.year, now.month, last_day_num, 23, 59, 59)

        return first_day, last_day

    @staticmethod
    def get_month_range(year: int, month: int) -> Tuple[datetime, datetime]:
        """
        Get the range of the specific month.
        Args:
            year (int): The year of the month.
            month (int): The month.
        Returns:
            Tuple[datetime, datetime]: A tuple containing the first day and last day of the month.
        """
        first_day = datetime(year, month, 3)
        last_day_num = monthrange(year, month)[1]
        last_day = datetime(year, month, last_day_num, 23, 59, 59)

        return first_day, last_day

    @staticmethod
    def get_year_range(year: int) -> Tuple[datetime, datetime]:
        """
        Get the range of the specific year.
        Args:
            year (int): The year.
        Returns:
            Tuple[datetime, datetime]: A tuple containing the first day and last day of the year.
        """
        first_day = datetime(year, 1, 1)
        last_day = datetime(year, 12, 31, 23, 59, 59)

        return first_day, last_day

    @staticmethod
    def format_date_range(start_date: datetime, end_date: datetime) -> str:
        """
        Get the range of date for show in the UI.
        Args:
            start_date (datetime): The start date.
            end_date (datetime): The end date.
        Returns:
            str: The range of date.
        """
        if start_date.year == end_date.year:
            if start_date.month == end_date.month:
                return f"{month_name[start_date.month]} {start_date.year}"
            else:
                return f"{start_date.strftime('%b')} - {end_date.strftime('%b')} {start_date.year}"
        else:
            return f"{start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')}"

    @staticmethod
    def get_last_n_days(days: int) -> Tuple[datetime, datetime]:
        """
        Get the range of the last n days.
        Args:
            days (int): The number of days.
        Returns:
            Tuple[datetime, datetime]: A tuple containing the first day and last day of the last n days.
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days - 1)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)

        return start_date, end_date

    @staticmethod
    def is_same_month(date1: datetime, date2: datetime) -> bool:
        """
        Check if two dates is the same month and year.
        Args:
            date1 (datetime): The first date.
            date2 (datetime): The second date.
        Returns:
            bool: True if the dates are the same month and year, False otherwise.
        """
        return date1.year == date2.year and date1.month == date2.month

    @staticmethod
    def parse_date_string(date_str: str) -> datetime:
        """
        Parse a date string into a datetime object.
        Args:
            date_str (str): The date string.
        Returns:
            datetime: The parsed datetime object.
        Raises:
            ValueError: If the date string is not in a recognized format.
        """
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%m/%d/%Y",
            "%d-%m-%Y",
            "%Y/%m/%d",
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

        raise ValueError(f"Date format not recognized: {date_str}")
