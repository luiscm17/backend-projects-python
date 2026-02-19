import unittest
import tempfile
import os
from src.utils.db_handler import DBHandler
from src.repositories.task_repository_db import TaskRepositoryDB
from src.models.task import Task


class TestTaskRepositoryDB(unittest.TestCase):
    """Test cases for TaskRepositoryDB"""

    def setUp(self):
        """Set up test repository"""
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "test_tasks.db")
        self.db_handler = DBHandler(self.db_path)
        self.repository = TaskRepositoryDB(self.db_handler)

    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        os.rmdir(self.temp_dir)

    def test_get_next_id_empty(self):
        """Test getting next ID when no tasks exist"""
        next_id = self.repository.get_next_id()
        self.assertEqual(next_id, 1)

    def test_get_next_id_with_tasks(self):
        """Test getting next ID when tasks exist"""
        task1 = Task(1, "Task 1", "todo")
        task2 = Task(2, "Task 2", "done")
        
        self.repository.save_task(task1)
        self.repository.save_task(task2)
        
        next_id = self.repository.get_next_id()
        self.assertEqual(next_id, 3)

    def test_save_task(self):
        """Test saving a task"""
        task = Task(1, "Test task", "todo")
        
        self.repository.save_task(task)
        
        tasks = self.repository.find_all()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Test task")
        self.assertEqual(tasks[0].status, "todo")

    def test_find_by_id_exists(self):
        """Test finding a task by ID when it exists"""
        task = Task(1, "Test task", "todo")
        self.repository.save_task(task)
        
        found_task = self.repository.find_by_id(1)
        
        self.assertIsNotNone(found_task)
        self.assertEqual(found_task.id, 1)
        self.assertEqual(found_task.description, "Test task")
        self.assertEqual(found_task.status, "todo")
        self.assertIsNotNone(found_task.created_at)
        self.assertIsNotNone(found_task.updated_at)

    def test_find_by_id_not_exists(self):
        """Test finding a task by ID when it doesn't exist"""
        found_task = self.repository.find_by_id(999)
        self.assertIsNone(found_task)

    def test_find_all(self):
        """Test finding all tasks"""
        task1 = Task(1, "Task 1", "todo")
        task2 = Task(2, "Task 2", "done")
        
        self.repository.save_task(task1)
        self.repository.save_task(task2)
        
        tasks = self.repository.find_all()
        self.assertEqual(len(tasks), 2)
        
        # Verify tasks have correct properties
        for task in tasks:
            self.assertIsNotNone(task.created_at)
            self.assertIsNotNone(task.updated_at)

    def test_find_by_status(self):
        """Test finding tasks by status"""
        task1 = Task(1, "Task 1", "todo")
        task2 = Task(2, "Task 2", "done")
        task3 = Task(3, "Task 3", "todo")
        
        self.repository.save_task(task1)
        self.repository.save_task(task2)
        self.repository.save_task(task3)
        
        todo_tasks = self.repository.find_by_status("todo")
        done_tasks = self.repository.find_by_status("done")
        
        self.assertEqual(len(todo_tasks), 2)
        self.assertEqual(len(done_tasks), 1)
        
        # Verify correct tasks are returned
        todo_ids = [task.id for task in todo_tasks]
        done_ids = [task.id for task in done_tasks]
        
        self.assertIn(1, todo_ids)
        self.assertIn(3, todo_ids)
        self.assertIn(2, done_ids)

    def test_update_task(self):
        """Test updating a task"""
        task = Task(1, "Original task", "todo")
        self.repository.save_task(task)
        
        # Update the task
        task.description = "Updated task"
        task.status = "done"
        task.updated_at = "2026-02-18T23:45:00.000000"
        
        self.repository.update_task(task)
        
        updated_task = self.repository.find_by_id(1)
        self.assertEqual(updated_task.description, "Updated task")
        self.assertEqual(updated_task.status, "done")
        self.assertEqual(updated_task.updated_at, "2026-02-18T23:45:00.000000")

    def test_delete_task(self):
        """Test deleting a task"""
        task = Task(1, "Test task", "todo")
        self.repository.save_task(task)
        
        # Delete the task
        result = self.repository.delete_task(1)
        
        self.assertTrue(result)
        
        tasks = self.repository.find_all()
        self.assertEqual(len(tasks), 0)

    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task"""
        result = self.repository.delete_task(999)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
