import unittest
import sys
import os
import tempfile
import shutil

# Add the parent directory to the path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.task import Task
from src.services.task_service import TaskService
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler


class TestTaskService(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_tasks.json")
        self.file_handler = FileHandler(self.test_file)
        self.repository = TaskRepository(self.file_handler)
        self.service = TaskService(self.repository)

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_add_task_success(self):
        """Test adding a task successfully"""
        task = self.service.add_task("Test Task")
        
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Test Task")
        self.assertEqual(task.status, "in-progress")
        self.assertEqual(task.id, 1)

    def test_add_task_empty_description(self):
        """Test adding a task with empty description"""
        with self.assertRaises(ValueError) as context:
            self.service.add_task("")
        
        self.assertEqual(str(context.exception), "Description cannot be empty")

    def test_add_task_whitespace_description(self):
        """Test adding a task with only whitespace description"""
        with self.assertRaises(ValueError) as context:
            self.service.add_task("   ")
        
        self.assertEqual(str(context.exception), "Description cannot be empty")

    def test_add_task_trims_whitespace(self):
        """Test that add_task trims whitespace from description"""
        task = self.service.add_task("  Test Task  ")
        
        self.assertEqual(task.description, "Test Task")

    def test_list_all_tasks_empty(self):
        """Test listing all tasks when none exist"""
        tasks = self.service.list_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_all_tasks_with_tasks(self):
        """Test listing all tasks when tasks exist"""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        
        tasks = self.service.list_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_list_tasks_by_status_valid(self):
        """Test listing tasks by valid status"""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        
        # Mark one task as done
        self.service.mark_task_done(task1.id)
        
        in_progress_tasks = self.service.list_tasks_by_status("in-progress")
        done_tasks = self.service.list_tasks_by_status("done")
        
        self.assertEqual(len(in_progress_tasks), 1)
        self.assertEqual(len(done_tasks), 1)

    def test_list_tasks_by_status_all(self):
        """Test listing all tasks using 'all' status"""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        
        all_tasks = self.service.list_tasks_by_status("all")
        self.assertEqual(len(all_tasks), 2)

    def test_list_tasks_by_status_invalid(self):
        """Test listing tasks by invalid status"""
        with self.assertRaises(ValueError) as context:
            self.service.list_tasks_by_status("invalid")
        
        self.assertEqual(str(context.exception), "Invalid status: Use 'all', 'in-progress' or 'done'")

    def test_update_task_success(self):
        """Test updating a task successfully"""
        task = self.service.add_task("Original Task")
        
        updated_task = self.service.update_task(task.id, "Updated Task")
        
        self.assertEqual(updated_task.description, "Updated Task")
        self.assertNotEqual(updated_task.updated_at, updated_task.created_at)

    def test_update_task_empty_description(self):
        """Test updating a task with empty description"""
        task = self.service.add_task("Test Task")
        
        with self.assertRaises(ValueError) as context:
            self.service.update_task(task.id, "")
        
        self.assertEqual(str(context.exception), "Description cannot be empty")

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist"""
        with self.assertRaises(ValueError) as context:
            self.service.update_task(999, "Updated Task")
        
        self.assertEqual(str(context.exception), "Task with id 999 not found")

    def test_delete_task_success(self):
        """Test deleting a task successfully"""
        task = self.service.add_task("Test Task")
        
        result = self.service.delete_task(task.id)
        self.assertTrue(result)
        
        # Verify task was deleted
        tasks = self.service.list_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist"""
        with self.assertRaises(ValueError) as context:
            self.service.delete_task(999)
        
        self.assertEqual(str(context.exception), "Task with id 999 not found")

    def test_mark_task_in_progress_success(self):
        """Test marking a task as in-progress successfully"""
        task = self.service.add_task("Test Task")
        
        updated_task = self.service.mark_task_in_progress(task.id)
        
        self.assertEqual(updated_task.status, "in-progress")
        self.assertNotEqual(updated_task.updated_at, updated_task.created_at)

    def test_mark_task_in_progress_not_found(self):
        """Test marking a non-existent task as in-progress"""
        with self.assertRaises(ValueError) as context:
            self.service.mark_task_in_progress(999)
        
        self.assertEqual(str(context.exception), "Task with ID 999 not found")

    def test_mark_task_done_success(self):
        """Test marking a task as done successfully"""
        task = self.service.add_task("Test Task")
        
        updated_task = self.service.mark_task_done(task.id)
        
        self.assertEqual(updated_task.status, "done")
        self.assertNotEqual(updated_task.updated_at, updated_task.created_at)

    def test_mark_task_done_not_found(self):
        """Test marking a non-existent task as done"""
        with self.assertRaises(ValueError) as context:
            self.service.mark_task_done(999)
        
        self.assertEqual(str(context.exception), "Task with ID 999 not found")


if __name__ == "__main__":
    unittest.main()
