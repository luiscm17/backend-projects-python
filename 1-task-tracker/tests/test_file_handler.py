import unittest
import sys
import os
import tempfile
import shutil
import json

# Add the parent directory to the path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_tasks.json")
        self.file_handler = FileHandler(self.test_file)

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_read_task_file_not_exists(self):
        """Test reading when file doesn't exist"""
        # Remove the file if it exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        tasks = self.file_handler.read_tasks()
        self.assertEqual(tasks, [])

    def test_read_task_empty_file(self):
        """Test reading from an empty file"""
        # Create empty file
        with open(self.test_file, "w") as f:
            f.write("")

        tasks = self.file_handler.read_tasks()
        self.assertEqual(tasks, [])

    def test_read_task_invalid_json(self):
        """Test reading from file with invalid JSON"""
        # Create file with invalid JSON
        with open(self.test_file, "w") as f:
            f.write("invalid json content")

        tasks = self.file_handler.read_tasks()
        self.assertEqual(tasks, [])

    def test_read_task_valid_json(self):
        """Test reading from file with valid JSON"""
        test_data = [
            {"id": 1, "description": "Task 1", "status": "in-progress"},
            {"id": 2, "description": "Task 2", "status": "done"},
        ]

        with open(self.test_file, "w") as f:
            json.dump(test_data, f)

        tasks = self.file_handler.read_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[1]["description"], "Task 2")

    def test_write_task_empty_list(self):
        """Test writing empty task list"""
        tasks = []
        self.file_handler.write_tasks(tasks)

        # Verify file was created and contains empty list
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_write_task_with_data(self):
        """Test writing task list with data"""
        tasks = [
            {"id": 1, "description": "Task 1", "status": "in-progress"},
            {"id": 2, "description": "Task 2", "status": "done"},
        ]

        self.file_handler.write_tasks(tasks)

        # Verify file was created and contains correct data
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], 1)
        self.assertEqual(data[1]["description"], "Task 2")

    def test_write_task_overwrites_existing(self):
        """Test that write_task overwrites existing content"""
        # Write initial data
        initial_tasks = [{"id": 1, "description": "Initial Task"}]
        self.file_handler.write_tasks(initial_tasks)

        # Write new data
        new_tasks = [{"id": 2, "description": "New Task"}]
        self.file_handler.write_tasks(new_tasks)

        # Verify only new data exists
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], 2)
        self.assertEqual(data[0]["description"], "New Task")

    def test_file_handler_with_default_filename(self):
        """Test FileHandler with default filename"""
        # Test with default filename (should create in data directory)
        handler = FileHandler()
        self.assertTrue(handler.filename.endswith("tasks.json"))
        self.assertTrue("data" in handler.filename)

    def test_file_handler_with_custom_filename(self):
        """Test FileHandler with custom filename"""
        custom_file = os.path.join(self.test_dir, "custom.json")
        handler = FileHandler(custom_file)
        self.assertEqual(handler.filename, custom_file)

    def test_data_directory_creation(self):
        """Test that data directory is created automatically"""
        # Create a handler with default filename (should create data directory)
        handler = FileHandler()

        # Get the data directory from the filename
        data_dir = os.path.dirname(handler.filename)

        # Verify directory was created
        self.assertTrue(os.path.exists(data_dir))
        self.assertTrue(os.path.isdir(data_dir))


if __name__ == "__main__":
    unittest.main()
