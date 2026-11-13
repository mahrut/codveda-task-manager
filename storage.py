
import json
from pathlib import Path


def load_tasks(file_path):
    """Load tasks from a JSON file."""

    path = Path(file_path)

    if not path.exists():
        save_tasks([], path)
        return []

    with path.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Invalid JSON data: expected a list.")

    if not all(isinstance(task, dict) for task in tasks):
        raise ValueError("Invalid JSON data: tasks must be objects.")

    return tasks


def save_tasks(tasks, file_path):
    """Save tasks to a JSON file."""

    path = Path(file_path)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
        file.write("\n")
