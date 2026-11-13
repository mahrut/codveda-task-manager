
from pathlib import Path

from task_manager import (
    add_task,
    get_task,
    update_task,
    mark_completed,
    delete_task
)

from storage import load_tasks, save_tasks


DATA_FILE = Path(__file__).with_name("tasks.json")


def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 45)
    print("           CODVEDA TASK MANAGER")
    print("=" * 45)

    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View task details")
    print("4. Update a task")
    print("5. Mark task as completed")
    print("6. Delete a task")
    print("7. Exit")

    print("=" * 45)


def save_data(tasks):
    """Save task data and handle file errors."""

    try:
        save_tasks(tasks, DATA_FILE)
        return True

    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False


def get_task_id():
    """Ask the user for a valid task ID."""

    try:
        task_id = int(input("Enter task ID: "))

        if task_id <= 0:
            print("Task ID must be a positive number.")
            return None

        return task_id

    except ValueError:
        print("Invalid input. Enter a numeric task ID.")
        return None


def add_new_task(tasks):
    """Receive information and create a task."""

    print("\n--- ADD NEW TASK ---")

    title = input("Task title: ")
    description = input("Task description: ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()

    try:
        task = add_task(
            tasks,
            title,
            description,
            priority,
            due_date
        )

        if save_data(tasks):
            print(f"\nTask added successfully! ID: {task['id']}")

    except ValueError as error:
        print(f"Error: {error}")


def view_all_tasks(tasks):
    """Display all saved tasks."""

    print("\n--- ALL TASKS ---")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        due_date = task["due_date"] or "Not specified"

        print("-" * 45)
        print(f"ID:          {task['id']}")
        print(f"Title:       {task['title']}")
        print(f"Priority:    {task['priority']}")
        print(f"Due date:    {due_date}")
        print(f"Status:      {status}")


def view_task_details(tasks):
    """Display complete information about one task."""

    print("\n--- VIEW TASK DETAILS ---")

    task_id = get_task_id()

    if task_id is None:
        return

    task = get_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print("\nTask Details")
    print("-" * 35)
    print(f"ID:          {task['id']}")
    print(f"Title:       {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Priority:    {task['priority']}")
    print(f"Due date:    {task['due_date'] or 'Not specified'}")
    print(f"Completed:   {task['completed']}")


def update_existing_task(tasks):
    """Update an existing task."""

    print("\n--- UPDATE TASK ---")

    task_id = get_task_id()

    if task_id is None:
        return

    task = get_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print("Press Enter to keep the current value.")
    print("For description or due date, enter '-' to clear it.")

    title = input(f"Title [{task['title']}]: ").strip()
    description = input(
        f"Description [{task['description']}]: "
    ).strip()
    priority = input(
        f"Priority [{task['priority']}]: "
    ).strip()
    due_date = input(
        f"Due date [{task['due_date'] or 'None'}]: "
    ).strip()

    title = title or task["title"]

    if description == "":
        description = task["description"]
    elif description == "-":
        description = ""

    priority = priority or task["priority"]

    if due_date == "":
        due_date = task["due_date"]
    elif due_date == "-":
        due_date = None

    try:
        updated = update_task(
            tasks,
            task_id,
            title,
            description,
            priority,
            due_date
        )

        if updated and save_data(tasks):
            print("Task updated successfully!")

    except ValueError as error:
        print(f"Error: {error}")


def complete_existing_task(tasks):
    """Mark a task as completed."""

    print("\n--- COMPLETE TASK ---")

    task_id = get_task_id()

    if task_id is None:
        return

    if mark_completed(tasks, task_id):
        if save_data(tasks):
            print("Task marked as completed successfully!")
    else:
        print("Task not found.")


def delete_existing_task(tasks):
    """Delete a task after confirmation."""

    print("\n--- DELETE TASK ---")

    task_id = get_task_id()

    if task_id is None:
        return

    task = get_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    confirmation = input(
        f"Delete '{task['title']}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        if delete_task(tasks, task_id):
            if save_data(tasks):
                print("Task deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    """Start the Task Manager application."""

    print("Initializing Codveda Task Manager...")

    try:
        tasks = load_tasks(DATA_FILE)

    except (OSError, ValueError) as error:
        print(f"Could not load tasks: {error}")
        print("Please check your tasks.json file.")
        return

    print("Tasks loaded successfully!")

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_new_task(tasks)

        elif choice == "2":
            view_all_tasks(tasks)

        elif choice == "3":
            view_task_details(tasks)

        elif choice == "4":
            update_existing_task(tasks)

        elif choice == "5":
            complete_existing_task(tasks)

        elif choice == "6":
            delete_existing_task(tasks)

        elif choice == "7":
            print("\nThank you for using Codveda Task Manager!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
