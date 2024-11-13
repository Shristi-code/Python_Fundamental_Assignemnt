# todo_operations.py

# List to store to-do items
todo_list = []

def add_task(task):
    """Add a new task to the to-do list."""
    todo_list.append(task)
    print(f"'{task}' added to the list.")

def delete_task(index):
    """Delete a task by index from the to-do list."""
    if 0 <= index < len(todo_list):
        removed_task = todo_list.pop(index)
        print(f"'{removed_task}' has been removed.")
    else:
        print("Invalid index. Please try again.")

def view_tasks():
    """Display all tasks in the to-do list."""
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list):
            print(f"{i}. {task}")
