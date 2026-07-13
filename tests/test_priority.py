"""Tests for the task priority feature."""

import pytest

from taskmanager import core


def test_add_task_defaults_priority_to_medium():
    tasks = core.add_task([], "Write report")
    assert tasks[0]["priority"] == "medium"


def test_add_task_accepts_explicit_priority():
    tasks = core.add_task([], "Fix bug", priority="high")
    assert tasks[0]["priority"] == "high"


def test_add_task_rejects_invalid_priority():
    with pytest.raises(ValueError):
        core.add_task([], "Bad task", priority="urgent")


def test_tasks_with_priority_filters_and_preserves_order():
    tasks = []
    tasks = core.add_task(tasks, "High one", "high")
    tasks = core.add_task(tasks, "Medium one", "medium")
    tasks = core.add_task(tasks, "Another high", "high")

    high_tasks = core.tasks_with_priority(tasks, "high")
    assert [task["title"] for task in high_tasks] == ["High one", "Another high"]
    assert tasks == [
        {"id": 1, "title": "High one", "done": False, "priority": "high"},
        {"id": 2, "title": "Medium one", "done": False, "priority": "medium"},
        {"id": 3, "title": "Another high", "done": False, "priority": "high"},
    ]


def test_tasks_with_priority_rejects_invalid_priority():
    with pytest.raises(ValueError):
        core.tasks_with_priority([], "critical")
