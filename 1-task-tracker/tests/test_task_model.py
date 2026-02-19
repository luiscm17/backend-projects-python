import unittest
import sys
import os

# Add the parent directory to the path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.task import Task


class TestTaskModel(unittest.TestCase):
    def setUp(self):
        self.task = Task(1, "Test Task")

    def test_task_creation(self):
        self.assertEqual(self.task.id, 1)
        self.assertEqual(self.task.description, "Test Task")
        self.assertEqual(self.task.status, "todo")
        self.assertIsNotNone(self.task.created_at)
        self.assertIsNotNone(self.task.updated_at)

    def test_task_update(self):
        self.task.update_description("Updated Task")
        self.assertEqual(self.task.description, "Updated Task")
        self.assertNotEqual(self.task.updated_at, self.task.created_at)

    def test_update_status(self):
        self.task.update_status("in-progress")
        self.assertEqual(self.task.status, "in-progress")

        with self.assertRaises(ValueError):
            self.task.update_status("invalid")


if __name__ == "__main__":
    unittest.main()
