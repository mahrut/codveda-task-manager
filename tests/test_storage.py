
import json
import pytest

from storage import load_tasks, save_tasks


def test_save_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    tasks = [
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice coding",
            "priority": "High",
            "due_date": "2026-11-15",
            "completed": False
        }
    ]

    save_tasks(tasks, file_path)

    assert file_path.exists()

    with file_path.open("r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == tasks


def test_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    tasks = [
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice coding",
            "priority": "High",
            "due_date": None,
            "completed": False
        }
    ]

    save_tasks(tasks, file_path)

    loaded_tasks = load_tasks(file_path)

    assert loaded_tasks == tasks


def test_load_missing_file(tmp_path):
    file_path = tmp_path / "new_tasks.json"

    tasks = load_tasks(file_path)

    assert tasks == []
    assert file_path.exists()


def test_load_invalid_json(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_tasks(file_path)


def test_load_json_that_is_not_a_list(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text('{"id": 1}', encoding="utf-8")

    with pytest.raises(ValueError):
        load_tasks(file_path)


def test_save_and_load_empty_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"

    save_tasks([], file_path)

    assert load_tasks(file_path) == []
