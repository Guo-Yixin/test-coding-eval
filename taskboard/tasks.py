from __future__ import annotations

from collections.abc import Iterable
from typing import Any


Task = dict[str, Any]


def filter_by_status(tasks: Iterable[Task], status: str | None = None) -> list[Task]:
    """Return tasks matching status; no filter returns every task."""

    rows = list(tasks)
    if status is None:
        return rows
    return [task for task in rows if task.get("status") == status]


def search_tasks(tasks: Iterable[Task], query: str) -> list[Task]:
    """Find tasks whose title contains query, preserving input order."""

    rows = list(tasks)
    if not query:
        return rows
    return [task for task in rows if query in str(task.get("title", ""))]


def sort_by_priority(tasks: Iterable[Task]) -> list[Task]:
    """Return tasks ordered by priority while preserving equal-priority order."""

    order = {"high": 0, "medium": 1, "low": 2}
    return sorted(tasks, key=lambda task: order.get(str(task.get("priority", "")).lower(), 99))
