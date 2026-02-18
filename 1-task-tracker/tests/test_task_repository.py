import unittest
import sys
import os
import tempfile
import shutil

# Add the parent directory to the path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.task import Task
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler


class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_tasks.json")
        self.file_handler = FileHandler(self.test_file)
        self.repository = TaskRepository(self.file_handler)

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_get_next_id_empty(self):
        """Test getting next ID when no tasks exist"""
        next_id = self.repository.get_next_id()
        self.assertEqual(next_id, 1)

    def test_get_next_id_with_tasks(self):
        """Test getting next ID when tasks exist"""
        # Create a task first
        task = Task(1, "Test Task")
        self.repository.save_task(task)
        
        next_id = self.repository.get_next_id()
        self.assertEqual(next_id, 2)

    def test_save_task(self):
        """Test saving a task"""
        task = Task(1, "Test Task")
        self.repository.save_task(task)
        
        # Verify task was saved
        saved_task = self.repository.find_by_id(1)
        self.assertIsNotNone(saved_task)
        self.assertEqual(saved_task.id, 1)
        self.assertEqual(saved_task.description, "Test Task")

    def test_find_by_id_exists(self):
        """Test finding task by ID when it exists"""
        task = Task(1, "Test Task")
        self.repository.save_task(task)
        
        found_task = self.repository.find_by_id(1)
        self.assertIsNotNone(found_task)
        self.assertEqual(found_task.id, 1)
        self.assertEqual(found_task.description, "Test Task")

    def test_find_by_id_not_exists(self):
        """Test finding task by ID when it doesn't exist"""
        found_task = self.repository.find_by_id(999)
        self.assertIsNone(found_task)

    def test_find_all_empty(self):
        """Test finding all tasks when none exist"""
        tasks = self.repository.find_all()
        self.assertEqual(len(tasks), 0)

    def test_find_all_with_tasks(self):
        """Test finding all tasks when tasks exist"""
        task1 = Task(1, "Task 1")
        task2 = Task(2, "Task 2")
        self.repository.save_task(task1)
        self.repository.save_task(task2)
        
        tasks = self.repository.find_all()
        self.assertEqual(len(tasks), 2)

    def test_find_by_status(self):
        """Test finding tasks by status"""
        task1 = Task(1, "Task 1", "in-progress")
        task2 = Task(2, "Task 2", "done")
        task3 = Task(3, "Task 3", "in-progress")
        self.repository.save_task(task1)
        self.repository.save_task(task2)
        self.repository.save_task(task3)
        
        in_progress_tasks = self.repository.find_by_status("in-progress")
        done_tasks = self.repository.find_by_status("done")
        
        self.assertEqual(len(in_progress_tasks), 2)
        self.assertEqual(len(done_tasks), 1)

    def test_update_task(self):
        """Test updating a task"""
        task = Task(1, "Original Task")
        self.repository.save_task(task)
        
        # Update the task
        task.description = "Updated Task"
        task.update_status("done")
        self.repository.update_task(task)
        
        # Verify update
        updated_task = self.repository.find_by_id(1)
        self.assertEqual(updated_task.description, "Updated Task")
        self.assertEqual(updated_task.status, "done")

    def test_delete_task_exists(self):
        """Test deleting a task when it exists"""
        task = Task(1, "Test Task")
        self.repository.save_task(task)
        
        result = self.repository.delete_task(1)
        self.assertTrue(result)
        
        # Verify task was deleted
        found_task = self.repository.find_by_id(1)
        self.assertIsNone(found_task)

    def test_delete_task_not_exists(self):
        """Test deleting a task when it doesn't exist"""
        result = self.repository.delete_task(999)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
