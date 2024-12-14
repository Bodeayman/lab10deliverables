import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import necessary functions and variables from the app module
from app import app, add_task, get_tasks, tasks

class TestToDoList(unittest.TestCase):
    
    def setUp(self):
        """Reset the tasks list before each test."""
        tasks.clear()
        self.client = app.test_client()

    def test_add_task_function(self):
        """Test adding a single task."""
        add_task("buy groceries")
        self.assertEqual(tasks, ["buy groceries"])
        self.assertEqual(len(tasks), 1)

    def test_add_multiple_tasks_function(self):
        """Test adding multiple tasks."""
        add_task("buy groceries")
        add_task("clean the house")
        self.assertEqual(tasks, ["buy groceries", "clean the house"])
        self.assertEqual(len(tasks), 2)

    def test_get_tasks_function(self):
        """Test retrieving tasks using the get_tasks function."""
        add_task("buy groceries")
        add_task("clean the house")
        retrieved_tasks = get_tasks()
        self.assertEqual(retrieved_tasks, ["buy groceries", "clean the house"])
        self.assertEqual(len(retrieved_tasks), 2)

    def test_empty_task_list_function(self):
        """Test that the task list is initially empty."""
        self.assertEqual(tasks, [])
        self.assertEqual(len(tasks), 0)

    def test_add_task_route(self):
        """Test the '/add-task' route for adding a task."""
        response = self.client.post('/add-task', data={'task': 'buy groceries'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'buy groceries', response.data)
        self.assertEqual(tasks, ["buy groceries"])

    def test_index_route(self):
        """Test the '/' route to display tasks."""
        add_task("buy groceries")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'buy groceries', response.data)

if __name__ == '__main__':
    unittest.main()
