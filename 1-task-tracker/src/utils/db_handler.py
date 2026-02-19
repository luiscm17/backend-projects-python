import sqlite3
import os
from typing import List, Dict, Any, Optional
from src.models.task import Task


class DBHandler:
    def __init__(self, db_path: str = "tasks.db"):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        self.db_path = os.path.join(data_dir, db_path)
        self._initialize_database()

    def _initialize_database(self):
        """
        Initialize the database
        """
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'todo',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    CHECK (status IN ('todo', 'in-progress', 'done'))
                )
                """
        )
        conn.commit()
        conn.close()

    def save_task(self, task: "Task") -> None:
        """
        Save a task to the database

        Args:
            task: Task to save
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO tasks (description, status, created_at, updated_at)
                VALUES (?, ?, ?, ?)
                """,
            (
                task.description,
                task.status,
                task.created_at,
                task.updated_at,
            ),
        )
        conn.commit()
        conn.close()

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks from the database

        Returns:
            List of all tasks
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT id, description, status, created_at, updated_at
                FROM tasks
                ORDER BY created_at DESC
                """
        )
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def update_task(self, task: "Task") -> None:
        """
        Update a task in the database

        Args:
            task: Task to update
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE tasks
                SET description = ?, status = ?, updated_at = ?
                WHERE id = ?
                """,
            (task.description, task.status, task.updated_at, task.id),
        )
        conn.commit()
        conn.close()

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the database

        Args:
            task_id: Task ID to delete

        Returns:
            True if task was deleted, False otherwise
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        result = cursor.rowcount > 0
        conn.close()
        return result
