# Simple Todo List Manager

A lightweight Python class for managing to-do lists with basic functionality.

## Features

- Add tasks to your to-do list
- Remove tasks from the list
- Mark tasks as complete or incomplete
- View all tasks, completed tasks, or incomplete tasks
- Clear all tasks from the list

## Usage

```python
from todo import TodoList

# Create a new to-do list
my_todos = TodoList()

# Add some tasks
my_todos.add_task("Buy groceries")
my_todos.add_task("Clean the house")
my_todos.add_task("Pay bills")

# Mark a task as complete
my_todos.mark_complete(0)  # Mark "Buy groceries" as complete

# Get all tasks
all_tasks = my_todos.get_all_tasks()

# Get only incomplete tasks
pending_tasks = my_todos.get_incomplete_tasks()

# Get only completed tasks
done_tasks = my_todos.get_complete_tasks()

# Remove a task
my_todos.remove_task(1)  # Remove "Clean the house"

# Clear all tasks
my_todos.clear_all_tasks()
```

## Running Tests

To run the unit tests:

```bash
python -m unittest test_todo.py
```

## Requirements

- Python 3.6 or higher

## License

This project is open source and available under the MIT License.
