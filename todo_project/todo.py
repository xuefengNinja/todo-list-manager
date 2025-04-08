class TodoList:
    """
    A simple class for managing a to-do list.
    
    This class provides functionality to add, remove, mark tasks as complete,
    and view tasks in a to-do list. It's designed to be easy to use and integrate
    into other applications.
    """
    
    def __init__(self):
        """Initialize an empty to-do list."""
        self.tasks = []
        
    def add_task(self, task):
        """
        Add a new task to the to-do list.
        
        Args:
            task (str): The task description to add.
            
        Returns:
            int: The index of the newly added task.
        """
        if not isinstance(task, str) or not task.strip():
            raise ValueError("Task must be a non-empty string")
            
        self.tasks.append({"description": task.strip(), "completed": False})
        return len(self.tasks) - 1
        
    def remove_task(self, index):
        """
        Remove a task from the to-do list.
        
        Args:
            index (int): The index of the task to remove.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.tasks):
            raise IndexError("Task index out of range")
            
        self.tasks.pop(index)
        
    def mark_complete(self, index):
        """
        Mark a task as complete.
        
        Args:
            index (int): The index of the task to mark as complete.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.tasks):
            raise IndexError("Task index out of range")
            
        self.tasks[index]["completed"] = True
        
    def mark_incomplete(self, index):
        """
        Mark a task as incomplete.
        
        Args:
            index (int): The index of the task to mark as incomplete.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < len(self.tasks):
            raise IndexError("Task index out of range")
            
        self.tasks[index]["completed"] = False
        
    def get_all_tasks(self):
        """
        Get all tasks in the to-do list.
        
        Returns:
            list: A list of all tasks.
        """
        return self.tasks
        
    def get_incomplete_tasks(self):
        """
        Get all incomplete tasks.
        
        Returns:
            list: A list of incomplete tasks.
        """
        return [task for task in self.tasks if not task["completed"]]
        
    def get_complete_tasks(self):
        """
        Get all completed tasks.
        
        Returns:
            list: A list of completed tasks.
        """
        return [task for task in self.tasks if task["completed"]]
        
    def clear_all_tasks(self):
        """Remove all tasks from the to-do list."""
        self.tasks = []
        
    def __len__(self):
        """Return the number of tasks in the to-do list."""
        return len(self.tasks)

