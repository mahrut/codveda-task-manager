
import pytest

from task_manager import (
    add_task,
    get_task,
    update_task,
    mark_completed,
    delete_task
)


@pytest.fixture
def sample_tasks():
    return [
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice functions",
            "priority": "High",
            "due_date": "2026-11-15",
            "completed": False
        }
    ]


def test_add_task():
    tasks = []

    task = add_task(
        tasks,
        "Learn Python",
        "Practice functions",
        "High",
        "2026-11-15"
    )

    assert len(tasks) == 1
    assert task["id"] == 1
    assert task["title"] == "Learn Python"
    assert task["priority"] == "High"
    assert task["completed"] is False


def test_add_multiple_tasks(sample_tasks):
    task = add_task(
        sample_tasks,
        "Learn JSON",
        "Practice JSON files",
        "Medium"
    )

    assert task["id"] == 2
    assert len(sample_tasks) == 2


def test_add_task_with_empty_title():
    with pytest.raises(ValueError):
        add_task([], "", "Description", "High")


def test_add_task_with_invalid_priority():
    with pytest.raises(ValueError):
        add_task([], "Learn Python", "", "Urgent")


def test_add_task_with_invalid_date():
    with pytest.raises(ValueError):
        add_task([], "Learn Python", "", "High", "15-11-2026")


def test_get_task(sample_tasks):
    task = get_task(sample_tasks, 1)

    assert task is not None
    assert task["title"] == "Learn Python"


def test_get_nonexistent_task(sample_tasks):
    task = get_task(sample_tasks, 99)

    assert task is None


def test_update_task(sample_tasks):
    result = update_task(
        sample_tasks,
        1,
        "Learn Advanced Python",
        "Practice OOP",
        "Medium",
        "2026-11-20"
    )

    assert result is True
    assert sample_tasks[0]["title"] == "Learn Advanced Python"
    assert sample_tasks[0]["priority"] == "Medium"


def test_update_nonexistent_task(sample_tasks):
    result = update_task(
        sample_tasks,
        99,
        "New title",
        "",
        "Low",
        None
    )

    assert result is False


def test_mark_completed(sample_tasks):
    result = mark_completed(sample_tasks, 1)

    assert result is True
    assert sample_tasks[0]["completed"] is True


def test_mark_nonexistent_task_completed(sample_tasks):
    result = mark_completed(sample_tasks, 99)

    assert result is False


def test_delete_task(sample_tasks):
    result = delete_task(sample_tasks, 1)

    assert result is True
    assert len(sample_tasks) == 0


def test_delete_nonexistent_task(sample_tasks):
    result = delete_task(sample_tasks, 99)

    assert result is False
    assert len(sample_tasks) == 1


def test_invalid_update_does_not_change_task(sample_tasks):
    original_title = sample_tasks[0]["title"]

    with pytest.raises(ValueError):
        update_task(
            sample_tasks,
            1,
            "",
            "New description",
            "High",
            None
        )

    assert sample_tasks[0]["title"] == original_title
