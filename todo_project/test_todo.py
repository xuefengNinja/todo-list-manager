import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):
    """Test cases for the TodoList class."""
    
    def setUp(self):
        """Set up a new TodoList instance for each test."""
        self.todo_list = TodoList()
        
    def test_add_task(self):
        """Test adding tasks to the list."""
        index = self.todo_list.add_task("Buy groceries")
        self.assertEqual(index, 0)
        self.assertEqual(len(self.todo_list), 1)
        self.assertEqual(self.todo_list.tasks[0]["description"], "Buy groceries")
        self.assertFalse(self.todo_list.tasks[0]["completed"])
        
        # Add another task
        index = self.todo_list.add_task("Clean the house")
        self.assertEqual(index, 1)
        self.assertEqual(len(self.todo_list), 2)
        
    def test_add_invalid_task(self):
        """Test adding invalid tasks."""
        with self.assertRaises(ValueError):
            self.todo_list.add_task("")
            
        with self.assertRaises(ValueError):
            self.todo_list.add_task("   ")
            
        with self.assertRaises(ValueError):
            self.todo_list.add_task(123)
            
    def test_remove_task(self):
        """Test removing tasks from the list."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")
        
        self.todo_list.remove_task(1)
        self.assertEqual(len(self.todo_list), 2)
        self.assertEqual(self.todo_list.tasks[0]["description"], "Task 1")
        self.assertEqual(self.todo_list.tasks[1]["description"], "Task 3")
        
    def test_remove_invalid_index(self):
        """Test removing tasks with invalid indices."""
        self.todo_list.add_task("Task 1")
        
        with self.assertRaises(IndexError):
            self.todo_list.remove_task(1)
            
        with self.assertRaises(IndexError):
            self.todo_list.remove_task(-1)
            
    def test_mark_complete(self):
        """Test marking tasks as complete."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        
        self.todo_list.mark_complete(0)
        self.assertTrue(self.todo_list.tasks[0]["completed"])
        self.assertFalse(self.todo_list.tasks[1]["completed"])
        
    def test_mark_incomplete(self):
        """Test marking tasks as incomplete."""
        self.todo_list.add_task("Task 1")
        self.todo_list.mark_complete(0)
        self.assertTrue(self.todo_list.tasks[0]["completed"])
        
        self.todo_list.mark_incomplete(0)
        self.assertFalse(self.todo_list.tasks[0]["completed"])
        
    def test_get_all_tasks(self):
        """Test getting all tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        
        tasks = self.todo_list.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["description"], "Task 1")
        self.assertEqual(tasks[1]["description"], "Task 2")
        
    def test_get_incomplete_tasks(self):
        """Test getting incomplete tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.mark_complete(0)
        
        incomplete = self.todo_list.get_incomplete_tasks()
        self.assertEqual(len(incomplete), 1)
        self.assertEqual(incomplete[0]["description"], "Task 2")
        
    def test_get_complete_tasks(self):
        """Test getting complete tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.mark_complete(0)
        
        complete = self.todo_list.get_complete_tasks()
        self.assertEqual(len(complete), 1)
        self.assertEqual(complete[0]["description"], "Task 1")
        
    def test_clear_all_tasks(self):
        """Test clearing all tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        
        self.todo_list.clear_all_tasks()
        self.assertEqual(len(self.todo_list), 0)
        self.assertEqual(self.todo_list.get_all_tasks(), [])
        
    def test_len_method(self):
        """Test the __len__ method."""
        self.assertEqual(len(self.todo_list), 0)
        
        self.todo_list.add_task("Task 1")
        self.assertEqual(len(self.todo_list), 1)
        
        self.todo_list.add_task("Task 2")
        self.assertEqual(len(self.todo_list), 2)
        
        self.todo_list.remove_task(0)
        self.assertEqual(len(self.todo_list), 1)

if __name__ == "__main__":
    unittest.main()
