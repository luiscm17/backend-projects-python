import unittest
import tempfile
import os
from src.utils.db_handler import DBHandler
from src.models.task import Task


class TestDBHandler(unittest.TestCase):
    """Test cases for DBHandler"""

    def setUp(self):
        """Set up test database"""
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_tasks.db")
        self.db_handler = DBHandler(self.db_path)

    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        os.rmdir(self.temp_dir)

    def test_database_initialization(self):
        """Test that database is initialized correctly"""
        # Database should be created and table should exist
        self.assertTrue(os.path.exists(self.db_path))
        
        # Test that we can query the table
        tasks = self.db_handler.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_save_task(self):
        """Test saving a task"""
        task = Task(1, "Test task", "todo")
        
        self.db_handler.save_task(task)
        
        tasks = self.db_handler.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
        self.assertEqual(tasks[0]["status"], "todo")
        self.assertIsNotNone(tasks[0]["created_at"])
        self.assertIsNotNone(tasks[0]["updated_at"])

    def test_get_all_tasks(self):
        """Test retrieving all tasks"""
        task1 = Task(1, "Task 1", "todo")
        task2 = Task(2, "Task 2", "done")
        
        self.db_handler.save_task(task1)
        self.db_handler.save_task(task2)
        
        tasks = self.db_handler.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Tasks should be ordered by created_at DESC
        self.assertEqual(tasks[0]["description"], "Task 2")
        self.assertEqual(tasks[1]["description"], "Task 1")

    def test_update_task(self):
        """Test updating a task"""
        task = Task(1, "Original task", "todo")
        self.db_handler.save_task(task)
        
        # Update the task
        task.description = "Updated task"
        task.status = "done"
        task.updated_at = "2026-02-18T23:45:00.000000"
        
        self.db_handler.update_task(task)
        
        tasks = self.db_handler.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Updated task")
        self.assertEqual(tasks[0]["status"], "done")
        self.assertEqual(tasks[0]["updated_at"], "2026-02-18T23:45:00.000000")

    def test_delete_task(self):
        """Test deleting a task"""
        task = Task(1, "Test task", "todo")
        self.db_handler.save_task(task)
        
        # Delete the task
        result = self.db_handler.delete_task(1)
        
        self.assertTrue(result)
        
        tasks = self.db_handler.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task"""
        result = self.db_handler.delete_task(999)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
