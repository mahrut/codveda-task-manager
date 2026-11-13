
from datetime import date


# Available task priorities
VALID_PRIORITIES = ("High", "Medium", "Low")


def validate_task(title, priority, due_date):
    """
    Validate task information before saving.

    Checks:
    - Task title is not empty.
    - Priority is High, Medium, or Low.
    - Due date follows YYYY-MM-DD format.
    """

    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    priority = priority.strip().capitalize()

    if priority not in VALID_PRIORITIES:
        raise ValueError(
            "Priority must be High, Medium, or Low."
        )

    if due_date:
        try:
            parsed_date = date.fromisoformat(due_date)

            if parsed_date.isoformat() != due_date:
                raise ValueError

        except ValueError:
            raise ValueError(
                "Due date must use YYYY-MM-DD format."
            )

    return title, priority, due_date or None


def get_task(tasks, task_id):
    """
    Find and return a task using its unique ID.

    Returns:
        dict: The matching task.
        None: If the task does not exist.
    """

    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def add_task(
    tasks,
    title,
    description="",
    priority="Medium",
    due_date=None
):
    """
    Create and add a new task.

    Automatically generates a unique task ID.
    """

    title, priority, due_date = validate_task(
        title,
        priority,
        due_date
    )

    new_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    task = {
        "id": new_id,
        "title": title,
        "description": description.strip(),
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    return task


def update_task(
    tasks,
    task_id,
    title,
    description,
    priority,
    due_date
):
    """
    Update an existing task.

    Returns:
        True: If the task was updated.
        False: If the task was not found.
    """

    task = get_task(tasks, task_id)

    if task is None:
        return False

    title, priority, due_date = validate_task(
        title,
        priority,
        due_date
    )

    task["title"] = title
    task["description"] = description.strip()
    task["priority"] = priority
    task["due_date"] = due_date

    return True


def mark_completed(tasks, task_id):
    """
    Mark a task as completed.

    Returns:
        True: If the task was found and updated.
        False: If the task does not exist.
    """

    task = get_task(tasks, task_id)

    if task is None:
        return False

    task["completed"] = True

    return True


def delete_task(tasks, task_id):
    """
    Delete a task using its unique ID.

    Returns:
        True: If the task was deleted.
        False: If the task does not exist.
    """

    task = get_task(tasks, task_id)

    if task is None:
        return False

    tasks.remove(task)

    return True
